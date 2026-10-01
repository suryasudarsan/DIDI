/**
 * VoiceSetu AI - Client Application Logic
 * Audio-First, Zero-Prior-Digital-Knowledge Engine
 * Handles Web Speech TTS/ASR, Web Audio DTMF synthesis, Ambient Noise Simulation,
 * IVR State Machine, WhatsApp Voice Notes, and SHG Worker Escalations.
 */

// Global State
const appState = {
  currentLang: 'hi',
  currentDialect: 'standard',
  sessionId: 'sess-' + Math.random().toString(36).substring(2, 9),
  inCall: false,
  callDuration: 0,
  callTimerInterval: null,
  earpieceMode: false,
  ambientNoiseDb: 30,
  currentNoiseType: 'quiet',
  confidenceScore: 0.95,
  isRecordingWa: false,
  schemesList: [],
  speechSpeed: 0.85,
  voicePitch: 1.0,
  recognition: null,
  isListeningMic: false,
  audioContext: null,
  noiseNode: null,
  lastSpokenText: ""
};

// Language Locales Map for Web Speech API
const LANG_LOCALE_MAP = {
  hi: 'hi-IN',
  ta: 'ta-IN',
  te: 'te-IN',
  ml: 'ml-IN',
  en: 'en-IN'
};

// DTMF Frequency Map (standard telephony)
const DTMF_FREQS = {
  '1': [697, 1209], '2': [697, 1336], '3': [697, 1477],
  '4': [770, 1209], '5': [770, 1336], '6': [770, 1477],
  '7': [852, 1209], '8': [852, 1336], '9': [852, 1477],
  '*': [941, 1209], '0': [941, 1336], '#': [941, 1477],
  'DIDI': [852, 1633]
};

// DOM Content Loaded Initializer
document.addEventListener('DOMContentLoaded', () => {
  initAudioContext();
  initSpeechRecognition();
  initEventListeners();
  loadSchemesCatalog();
  loadWorkerTickets();
});

// Initialize Web Audio Context for DTMF & Noise Generation
function initAudioContext() {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {
      appState.audioContext = new AudioCtx();
    }
  } catch (e) {
    console.warn("AudioContext not supported:", e);
  }
}

// Play DTMF Tone on Keypad Press
function playDTMFTone(key) {
  if (!appState.audioContext) return;
  if (appState.audioContext.state === 'suspended') {
    appState.audioContext.resume();
  }

  const freqs = DTMF_FREQS[key];
  if (!freqs) return;

  const ctx = appState.audioContext;
  const osc1 = ctx.createOscillator();
  const osc2 = ctx.createOscillator();
  const gain = ctx.createGain();

  osc1.type = 'sine';
  osc2.type = 'sine';
  osc1.frequency.value = freqs[0];
  osc2.frequency.value = freqs[1];

  gain.gain.setValueAtTime(appState.earpieceMode ? 0.05 : 0.25, ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.18);

  osc1.connect(gain);
  osc2.connect(gain);
  gain.connect(ctx.destination);

  osc1.start();
  osc2.start();
  osc1.stop(ctx.currentTime + 0.18);
  osc2.stop(ctx.currentTime + 0.18);
}

// Spoken Audio TTS Engine with Indic Fallback
function speakAloud(text, onComplete) {
  if (!text) return;
  appState.lastSpokenText = text;

  // Visual Wave Animation trigger
  const wave = document.querySelector('.audio-wave-container');
  if (wave) wave.classList.add('speaking');

  // Display text in subtitle box
  const subtitleBox = document.getElementById('spokenPromptText');
  if (subtitleBox) subtitleBox.textContent = text;

  // Use Web Speech Synthesis
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel(); // Stop prior audio

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = LANG_LOCALE_MAP[appState.currentLang] || 'hi-IN';
    utterance.rate = parseFloat(appState.speechSpeed);
    utterance.pitch = parseFloat(appState.voicePitch);
    utterance.volume = appState.earpieceMode ? 0.25 : 1.0;

    // Pick appropriate localized voice if available
    const voices = window.speechSynthesis.getVoices();
    const langCode = LANG_LOCALE_MAP[appState.currentLang];
    const matchingVoice = voices.find(v => v.lang === langCode || v.lang.startsWith(appState.currentLang));
    if (matchingVoice) {
      utterance.voice = matchingVoice;
    }

    utterance.onend = () => {
      if (wave) wave.classList.remove('speaking');
      if (onComplete) onComplete();
    };

    utterance.onerror = (e) => {
      console.warn("Speech synthesis error or cancelled:", e);
      if (wave) wave.classList.remove('speaking');
      if (onComplete) onComplete();
    };

    window.speechSynthesis.speak(utterance);
  } else {
    // Fallback if browser lacks Web Speech API
    console.log("Audio speech synthesis fallback:", text);
    setTimeout(() => {
      if (wave) wave.classList.remove('speaking');
      if (onComplete) onComplete();
    }, 3000);
  }
}

// Initialize Speech Recognition for Hands-Free Speaking
function initSpeechRecognition() {
  const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRec) {
    appState.recognition = new SpeechRec();
    appState.recognition.continuous = false;
    appState.recognition.interimResults = false;
    appState.recognition.lang = LANG_LOCALE_MAP[appState.currentLang] || 'hi-IN';

    appState.recognition.onstart = () => {
      appState.isListeningMic = true;
      const micBtn = document.getElementById('toggleMicBtn');
      if (micBtn) {
        micBtn.classList.add('listening');
        micBtn.querySelector('.label').textContent = 'Listening...';
      }
    };

    appState.recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      console.log("Recognized speech:", transcript);
      handleUserInput(transcript);
    };

    appState.recognition.onerror = (err) => {
      console.warn("Speech recognition error:", err);
      resetMicUI();
    };

    appState.recognition.onend = () => {
      resetMicUI();
    };
  }
}

function resetMicUI() {
  appState.isListeningMic = false;
  const micBtn = document.getElementById('toggleMicBtn');
  if (micBtn) {
    micBtn.classList.remove('listening');
    micBtn.querySelector('.label').textContent = 'Speak Voice';
  }
}

// Ambient Noise Generator (Web Audio API)
function setAmbientNoise(type, db) {
  appState.currentNoiseType = type;
  appState.ambientNoiseDb = db;

  // Update UI Elements
  document.getElementById('noiseTag').textContent = `${type.toUpperCase()} (${db} dB)`;
  document.getElementById('currentDbLabel').textContent = `${db} dB`;
  const fillPct = Math.min(100, Math.max(10, (db / 90) * 100));
  document.getElementById('noiseMeterFill').style.width = `${fillPct}%`;

  // Update confidence score based on noise
  if (db <= 40) {
    appState.confidenceScore = 0.96;
  } else if (db <= 65) {
    appState.confidenceScore = 0.78;
  } else {
    appState.confidenceScore = 0.52; // Triggers low confidence auto-escalation
  }

  const confVal = document.getElementById('confidenceVal');
  const confPill = document.getElementById('confidencePill');
  confVal.textContent = `${Math.round(appState.confidenceScore * 100)}%`;

  if (appState.confidenceScore >= 0.70) {
    confPill.className = 'status-pill status-good';
    confPill.textContent = 'Clear Speech';
  } else {
    confPill.className = 'status-pill status-low';
    confPill.textContent = 'High Noise - Human Fallback Triggered';
  }
}

// Main Event Listeners
function initEventListeners() {
  // Mode Tabs Switching
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.mode-section').forEach(s => s.classList.remove('active'));

      btn.classList.add('active');
      const targetId = btn.getAttribute('data-target');
      document.getElementById(targetId).classList.add('active');
    });
  });

  // Language Buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      appState.currentLang = btn.getAttribute('data-lang');
      if (appState.recognition) {
        appState.recognition.lang = LANG_LOCALE_MAP[appState.currentLang];
      }
      // Re-filter catalog and reload tickets
      loadSchemesCatalog();
      if (appState.inCall) {
        handleUserInput("repeat");
      }
    });
  });

  // Dialect Select
  document.getElementById('dialectSelect').addEventListener('change', (e) => {
    appState.currentDialect = e.target.value;
  });

  // Speech Speed & Pitch Sliders
  document.getElementById('speechRate').addEventListener('input', (e) => {
    appState.speechSpeed = e.target.value;
    document.getElementById('rateValue').textContent = `${e.target.value}x (${e.target.value < 0.9 ? 'Slow & Clear' : 'Normal'})`;
  });

  document.getElementById('voicePitch').addEventListener('input', (e) => {
    appState.voicePitch = e.target.value;
  });

  // Keypad DTMF Buttons
  document.querySelectorAll('.key-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.getAttribute('data-key');
      playDTMFTone(key);

      if (key === 'DIDI') {
        triggerHumanEscalation("Direct One-Touch Keypad Escalation to SHG Didi");
      } else if (key === '*') {
        triggerCamouflageMode();
      } else {
        handleUserInput(key);
      }
    });
  });

  // Call Start / End Toggle Button
  document.getElementById('toggleCallBtn').addEventListener('click', toggleCall);

  // Microphone Speak Button
  document.getElementById('toggleMicBtn').addEventListener('click', () => {
    if (!appState.inCall) {
      alert("Please start the call first.");
      return;
    }
    if (appState.isListeningMic) {
      if (appState.recognition) appState.recognition.stop();
      resetMicUI();
    } else {
      if (appState.recognition) {
        try {
          appState.recognition.start();
        } catch (e) {
          console.warn("Recognition start error:", e);
        }
      } else {
        // Fallback prompt dialog
        const text = prompt("Speak/Type your answer (Haan/1, Nahin/2, Beti, Bachha, SHG):");
        if (text) handleUserInput(text);
      }
    }
  });

  // Earpiece Mode Toggle Button
  document.getElementById('toggleEarpieceBtn').addEventListener('click', () => {
    appState.earpieceMode = !appState.earpieceMode;
    const btn = document.getElementById('toggleEarpieceBtn');
    const label = document.getElementById('earpieceLabel');
    if (appState.earpieceMode) {
      btn.classList.add('active');
      label.textContent = 'Earpiece (Whisper)';
    } else {
      btn.classList.remove('active');
      label.textContent = 'Speaker';
    }
  });

  // Replay Audio (9)
  document.getElementById('replayPromptBtn').addEventListener('click', () => {
    if (appState.lastSpokenText) {
      speakAloud(appState.lastSpokenText);
    } else {
      handleUserInput("9");
    }
  });

  // Quick Panic / Camouflage Buttons
  document.getElementById('quickPanicBtn').addEventListener('click', triggerCamouflageMode);
  document.getElementById('exitCamouBtn').addEventListener('click', exitCamouflageMode);

  // Ambient Noise Simulator Presets
  document.querySelectorAll('.btn-noise').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.btn-noise').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const noise = btn.getAttribute('data-noise');
      const db = parseFloat(btn.getAttribute('data-db'));
      setAmbientNoise(noise, db);
    });
  });

  // Direct Escalation Button
  document.getElementById('directEscalateBtn').addEventListener('click', () => {
    triggerHumanEscalation("Direct One-Touch Screen Escalation Button Pressed");
  });
  document.getElementById('btnCallSHG').addEventListener('click', () => {
    triggerHumanEscalation("One-Touch Keypad Button 👩‍💼 SHG Didi Pressed");
  });

  // WhatsApp Voice Note Simulation
  document.getElementById('waRecordVoiceBtn').addEventListener('click', recordWaVoiceNote);
  document.querySelectorAll('.btn-quick-voice').forEach(btn => {
    btn.addEventListener('click', () => {
      const msg = btn.getAttribute('data-msg');
      simulateWhatsAppAudioNote(msg);
    });
  });

  // Scheme Filters
  document.getElementById('stateFilter').addEventListener('change', loadSchemesCatalog);
  document.getElementById('categoryFilter').addEventListener('change', loadSchemesCatalog);
}

// Start or End Call
async function toggleCall() {
  const callBtn = document.getElementById('toggleCallBtn');
  const avatar = document.getElementById('callAvatar');
  const statusText = document.getElementById('callStatusText');

  if (!appState.inCall) {
    // Start Call
    appState.inCall = true;
    appState.callDuration = 0;
    callBtn.classList.add('in-call');
    callBtn.querySelector('.label').textContent = 'End Call';
    avatar.classList.add('active-calling');
    statusText.textContent = 'Live Audio Connected • Toll-Free';

    // Start Call Timer
    appState.callTimerInterval = setInterval(() => {
      appState.callDuration++;
      const mins = String(Math.floor(appState.callDuration / 60)).padStart(2, '0');
      const secs = String(appState.callDuration % 60).padStart(2, '0');
      document.getElementById('callTimer').textContent = `${mins}:${secs}`;
    }, 1000);

    // Call API /api/ivr/start
    try {
      const res = await fetch('/api/ivr/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: appState.sessionId,
          language: appState.currentLang,
          dialect: appState.currentDialect
        })
      });
      const data = await res.json();
      speakAloud(data.audio_text);
    } catch (err) {
      console.error("Error starting IVR:", err);
      speakAloud("नमस्ते दीदी! यह भारत सरकार की ग्रामीण महिला कल्याण वॉइस सेवा है। आगे बढ़ने के लिए 1 दबाएं।");
    }
  } else {
    // End Call
    appState.inCall = false;
    clearInterval(appState.callTimerInterval);
    document.getElementById('callTimer').textContent = '00:00';
    callBtn.classList.remove('in-call');
    callBtn.querySelector('.label').textContent = 'Start Call';
    avatar.classList.remove('active-calling');
    statusText.textContent = 'Call Ended';
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    document.getElementById('spokenPromptText').textContent = 'Call ended. Press "Start Call" to begin a new session.';
  }
}

// Handle User Input (DTMF Key or Spoken Transcript)
async function handleUserInput(input) {
  if (!appState.inCall) {
    // If not in call, automatically start call first
    await toggleCall();
  }

  try {
    const res = await fetch('/api/ivr/input', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: appState.sessionId,
        user_input: input,
        language: appState.currentLang,
        ambient_noise_db: appState.ambientNoiseDb
      })
    });
    const data = await res.json();

    if (data.action === 'CAMOUFLAGE') {
      triggerCamouflageMode();
    } else if (data.action === 'ESCALATE_HUMAN') {
      speakAloud(data.audio_text);
      loadWorkerTickets(); // Refresh tickets in console
    } else if (data.action === 'END_CALL') {
      speakAloud(data.audio_text, () => {
        toggleCall();
      });
    } else {
      speakAloud(data.audio_text);
    }
  } catch (err) {
    console.error("Error sending input:", err);
  }
}

// Trigger One-Touch Human Escalation
async function triggerHumanEscalation(reason) {
  try {
    const res = await fetch('/api/ivr/escalate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: appState.sessionId,
        caller_phone: '+91 98765-43210',
        language: appState.currentLang,
        dialect: appState.currentDialect,
        reason: reason
      })
    });
    const data = await res.json();
    speakAloud(data.audio_text);
    loadWorkerTickets();
    alert("Call escalated to village SHG Bank Sakhi Sunita Devi (Rampur Gram Panchayat). Line bridging active.");
  } catch (err) {
    console.error("Escalation error:", err);
  }
}

// Trigger Privacy Camouflage Mode
async function triggerCamouflageMode() {
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  const overlay = document.getElementById('camouflageScreen');
  overlay.classList.remove('hidden');

  try {
    const res = await fetch(`/api/ivr/camouflage?mode=weather&lang=${appState.currentLang}`);
    const data = await res.json();
    document.getElementById('camouTitle').textContent = data.screen_title;
    speakAloud(data.audio_script);
  } catch (e) {
    speakAloud("दैनिक मौसम रिपोर्ट: आज आपके क्षेत्र में मौसम साफ रहेगा।");
  }
}

function exitCamouflageMode() {
  document.getElementById('camouflageScreen').classList.add('hidden');
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
}

// WhatsApp Voice Note Simulation
function recordWaVoiceNote() {
  if (!appState.isRecordingWa) {
    appState.isRecordingWa = true;
    const btn = document.getElementById('waRecordVoiceBtn');
    btn.classList.add('recording');
    document.getElementById('waMicStatus').textContent = 'Recording Voice Note... (Click to Send)';

    if (appState.recognition) {
      try {
        appState.recognition.start();
        appState.recognition.onresult = (e) => {
          const text = e.results[0][0].transcript;
          simulateWhatsAppAudioNote(text);
          stopWaRecording();
        };
      } catch (err) {
        console.warn(err);
      }
    }
  } else {
    stopWaRecording();
    simulateWhatsAppAudioNote("मेरी 8 साल की बेटी है, मुझे सुकन्या योजना की जानकारी चाहिए");
  }
}

function stopWaRecording() {
  appState.isRecordingWa = false;
  const btn = document.getElementById('waRecordVoiceBtn');
  btn.classList.remove('recording');
  document.getElementById('waMicStatus').textContent = 'Click to Record Voice Note';
  if (appState.recognition) appState.recognition.stop();
}

async function simulateWhatsAppAudioNote(transcript) {
  const chatWindow = document.getElementById('waChatWindow');

  // Append outgoing voice note bubble
  const outgoing = document.createElement('div');
  outgoing.className = 'wa-bubble wa-outgoing';
  outgoing.innerHTML = `
    <div class="bubble-meta">You (Rural Caller) • Just now</div>
    <div class="wa-voice-player">
      <button class="btn-wa-play">▶</button>
      <div class="wa-waveform playing">
        <span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
      <span class="wa-duration">0:06</span>
    </div>
    <p class="wa-transcript">"${transcript}"</p>
  `;
  chatWindow.appendChild(outgoing);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  // Send to backend
  try {
    const res = await fetch('/api/whatsapp/voice-note', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        caller_phone: '+91 98765-43210',
        language: appState.currentLang,
        audio_transcript: transcript
      })
    });
    const data = await res.json();

    // Append incoming voice note bubble
    const incoming = document.createElement('div');
    incoming.className = 'wa-bubble wa-incoming';
    incoming.innerHTML = `
      <div class="bubble-meta">VoiceSetu Helpline • Just now</div>
      <div class="wa-voice-player">
        <button class="btn-wa-play">▶</button>
        <div class="wa-waveform playing">
          <span></span><span></span><span></span><span></span><span></span><span></span>
        </div>
        <span class="wa-duration">0:18</span>
      </div>
      <p class="wa-transcript">"${data.reply_audio_text}"</p>
    `;
    chatWindow.appendChild(incoming);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Speak reply
    speakAloud(data.reply_audio_text);
  } catch (err) {
    console.error("WhatsApp simulation error:", err);
  }
}

// Load All-India Schemes from RAG Endpoint
async function loadSchemesCatalog() {
  const stateVal = document.getElementById('stateFilter').value;
  const catVal = document.getElementById('categoryFilter').value;

  let url = '/api/schemes';
  const params = [];
  if (stateVal && stateVal !== 'all') params.push(`state=${encodeURIComponent(stateVal)}`);
  if (catVal && catVal !== 'all') params.push(`category=${encodeURIComponent(catVal)}`);
  if (params.length > 0) url += '?' + params.join('&');

  try {
    const res = await fetch(url);
    const data = await res.json();
    appState.schemesList = data.schemes;

    document.getElementById('schemeStats').innerHTML = `Showing <strong>${data.schemes.length}</strong> Official Schemes`;
    renderSchemeCards(data.schemes);
  } catch (err) {
    console.error("Error loading schemes:", err);
  }
}

// Render Scheme Cards in Glass Grid
function renderSchemeCards(schemes) {
  const grid = document.getElementById('schemeGrid');
  grid.innerHTML = '';

  schemes.forEach(s => {
    const card = document.createElement('div');
    card.className = 'scheme-card glass-panel';

    const vernacularName = s.vernacular_names[appState.currentLang] || s.vernacular_names['hi'] || s.name;
    const desc = s.descriptions[appState.currentLang] || s.descriptions['en'] || '';
    const docs = s.documents_required || [];

    const docTags = docs.map(d => {
      const docName = (d.vernacular && d.vernacular[appState.currentLang]) ? d.vernacular[appState.currentLang] : d.doc;
      return `<span class="doc-tag">📄 ${docName}</span>`;
    }).join('');

    card.innerHTML = `
      <div>
        <div class="card-top">
          <span class="scheme-scope-badge ${s.scope === 'Central' ? 'central' : 'state'}">${s.scope}</span>
          <span class="badge-accent">${s.category.toUpperCase()}</span>
        </div>
        <h3>${s.name}</h3>
        <p class="vernacular-title">${vernacularName}</p>
        <span class="benefit-pill">💰 ${s.benefit_amount}</span>
        <p class="scheme-desc">${desc}</p>
        <div class="doc-tag-list">${docTags}</div>
      </div>
      <div class="card-actions">
        <button class="btn-card-audio" onclick="playSchemeAudio('${s.id}')">
          <span>🔊</span>
          <span>Listen Audio Summary</span>
        </button>
        <button class="btn-card-apply" onclick="showOfflineGuide('${s.id}')">
          <span>📍 Offline Walkthrough</span>
        </button>
      </div>
    `;
    grid.appendChild(card);
  });
}

// Play Audio Summary for a Given Scheme
window.playSchemeAudio = function(schemeId) {
  const scheme = appState.schemesList.find(s => s.id === schemeId);
  if (!scheme) return;

  const vernName = scheme.vernacular_names[appState.currentLang] || scheme.name;
  const desc = scheme.descriptions[appState.currentLang] || scheme.descriptions['hi'];
  const audioText = `${vernName}। ${desc} लाभ: ${scheme.benefit_amount}। आवश्यक दस्तावेज: आधार कार्ड और बैंक पासबुक।`;
  speakAloud(audioText);
};

// Show Offline Center & Token Guidance
window.showOfflineGuide = function(schemeId) {
  const scheme = appState.schemesList.find(s => s.id === schemeId);
  if (!scheme) return;

  const off = scheme.offline_process;
  const alertText = `Offline Center: ${off.submission_center}\n\nAction: ${off.action}\n\nToken Prefix: ${off.token_code_prefix}`;
  alert(alertText);

  // Also speak it aloud
  const spokenText = `इस योजना के लिए आवेदन करने का केंद्र है: ${off.submission_center}। अपने गांव के केंद्र पर आधार कार्ड और बैंक खाता लेकर जाएं।`;
  speakAloud(spokenText);
};

// Load Worker Fallback Tickets
async function loadWorkerTickets() {
  try {
    const res = await fetch('/api/fallback/queue');
    const data = await res.json();
    const tbody = document.getElementById('ticketsBody');
    tbody.innerHTML = '';

    data.tickets.forEach(t => {
      const tr = document.createElement('tr');
      let statusClass = 'status-scheduled';
      if (t.status === 'LIVE_CONNECTING' || t.status === 'PENDING_CALL') statusClass = 'status-live';
      if (t.status === 'RESOLVED') statusClass = 'status-resolved';

      tr.innerHTML = `
        <td>${t.id}</td>
        <td>
          <strong>${t.caller_phone}</strong><br>
          <small style="color:#64748b">${t.village || 'Gram Panchayat'}</small>
        </td>
        <td><span class="badge-noise">${t.language.toUpperCase()} (${t.dialect})</span></td>
        <td><strong>${t.target_scheme}</strong></td>
        <td><small style="color:#dc2626">${t.missing_docs ? t.missing_docs.join(', ') : t.reason}</small></td>
        <td><strong>${t.assigned_worker}</strong></td>
        <td><span class="table-status-pill ${statusClass}">${t.status}</span></td>
        <td>
          <button class="btn-table-action" onclick="resolveTicket('${t.id}')">Doorstep Visit</button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error("Error loading tickets:", err);
  }
}

// Worker Action: Resolve Ticket / Schedule Doorstep Visit
window.resolveTicket = async function(ticketId) {
  try {
    await fetch('/api/fallback/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ticket_id: ticketId,
        status: 'DOORSTEP_SCHEDULED',
        notes: 'Doorstep physical biometric verification scheduled with micro-ATM.'
      })
    });
    alert(`Ticket ${ticketId}: Doorstep visit scheduled with Bank Sakhi micro-ATM!`);
    loadWorkerTickets();
  } catch (err) {
    console.error("Error updating ticket:", err);
  }
};
