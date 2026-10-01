"""
VoiceSetu Backend - FastAPI Server
Integrates RAG Knowledge Base, IVR Audio State Machine, WhatsApp Voice Notes,
Human Intermediary Fallback, and Discreet Safety Camouflage.
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os

from backend.schemes_rag import get_all_schemes, get_scheme_by_id, search_schemes
from backend.dialogue_engine import get_or_create_session, LOCALIZED_PROMPTS
from backend.human_fallback import get_fallback_queue, create_fallback_ticket, update_ticket_status
from backend.safety_camouflage import get_camouflage_payload

app = FastAPI(
    title="VoiceSetu AI - Audio-First Welfare Access for Rural Indian Women",
    description="Zero-prior-digital-knowledge voice assistant with IVR, WhatsApp Voice Notes, RAG and Human Fallback",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic schemas
class IVRStartRequest(BaseModel):
    session_id: Optional[str] = None
    language: str = "hi"
    dialect: str = "standard"
    caller_phone: Optional[str] = "+91 98765-43210"

class IVRInputRequest(BaseModel):
    session_id: str
    user_input: str
    language: Optional[str] = "hi"
    ambient_noise_db: Optional[float] = 30.0

class IVREscalateRequest(BaseModel):
    session_id: str
    caller_phone: Optional[str] = "+91 98765-43210"
    language: str = "hi"
    target_scheme: Optional[str] = "PMMVY (Maternity Assistance)"
    missing_docs: Optional[List[str]] = []
    reason: str = "One-Touch SHG Didi Fallback Button Pressed"
    dialect: Optional[str] = "Standard"

class WhatsAppVoiceRequest(BaseModel):
    caller_phone: str = "+91 98765-43210"
    language: str = "hi"
    audio_transcript: str
    audio_duration_seconds: Optional[float] = 4.5

class TicketUpdateRequest(BaseModel):
    ticket_id: str
    status: str
    notes: Optional[str] = None

# Scheme Endpoints (RAG)
@app.get("/api/schemes")
def list_schemes(
    state: Optional[str] = None,
    category: Optional[str] = None,
    marital_status: Optional[str] = None
):
    """Retrieve all or filtered official schemes for Indian rural women."""
    if state or category or marital_status:
        results = search_schemes(user_state=state, category_filter=category, marital_status=marital_status)
    else:
        results = get_all_schemes()
    return {
        "status": "success",
        "total_schemes": len(results),
        "schemes": results
    }

@app.get("/api/schemes/{scheme_id}")
def get_scheme(scheme_id: str):
    scheme = get_scheme_by_id(scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return {"status": "success", "scheme": scheme}

# IVR Dialogue Endpoints
@app.post("/api/ivr/start")
def start_ivr(req: IVRStartRequest):
    """Starts an audio-first IVR phone call simulation."""
    session = get_or_create_session(req.session_id, lang=req.language, dialect=req.dialect)
    greeting_text = session.get_prompt("greeting_consent")
    repeat_hint = session.get_prompt("repeat_hint")

    return {
        "session_id": session.session_id,
        "state": session.state,
        "language": session.lang,
        "dialect": session.dialect,
        "audio_text": f"{greeting_text} {repeat_hint}",
        "dtmf_options": [
            {"key": "1", "label": "1: Haan / Agree (सहमति)"},
            {"key": "2", "label": "2: Nahin / Disagree"},
            {"key": "9", "label": "9: Phir se sunein (Repeat)"},
            {"key": "*", "label": "*: Gupt Mausam (Panic Hide)"}
        ]
    }

@app.post("/api/ivr/input")
def process_ivr_input(req: IVRInputRequest):
    """Processes DTMF keypad or voice response, evaluating ambient noise."""
    session = get_or_create_session(req.session_id, lang=req.language or "hi")
    response = session.process_input(req.user_input, ambient_noise_db=req.ambient_noise_db or 30.0)

    # If action is ESCALATE_HUMAN, automatically register a fallback ticket
    if response.get("action") == "ESCALATE_HUMAN":
        ticket = create_fallback_ticket(
            session_id=session.session_id,
            caller_phone="+91 98765-43210",
            language=session.lang,
            target_scheme=session.matched_schemes[0]["name"] if session.matched_schemes else "Maternity/SHG Scheme",
            missing_docs=["Aadhaar-Bank Passbook Verification"],
            reason=response.get("reason", "Voice clarity low / user requested human worker"),
            dialect=session.dialect
        )
        response["ticket"] = ticket

    return {
        "session_id": session.session_id,
        "confidence_score": session.confidence_score,
        "escalated": session.escalated,
        **response
    }

@app.post("/api/ivr/escalate")
def escalate_to_human(req: IVREscalateRequest):
    """Direct one-touch button to connect with village SHG worker or CSC operator."""
    ticket = create_fallback_ticket(
        session_id=req.session_id,
        caller_phone=req.caller_phone,
        language=req.language,
        target_scheme=req.target_scheme,
        missing_docs=req.missing_docs,
        reason=req.reason,
        dialect=req.dialect
    )
    lang_dict = LOCALIZED_PROMPTS.get(req.language, LOCALIZED_PROMPTS["hi"])
    reassure_audio = lang_dict.get("fallback_reassure")

    return {
        "status": "escalated",
        "audio_text": reassure_audio,
        "ticket": ticket
    }

@app.get("/api/ivr/camouflage")
def get_camouflage(mode: str = "weather", lang: str = "hi"):
    """Emergency discreet mode payload."""
    return get_camouflage_payload(mode=mode, lang=lang)

# WhatsApp Voice Notes simulation
@app.post("/api/whatsapp/voice-note")
def process_whatsapp_voice(req: WhatsAppVoiceRequest):
    """
    Simulates a voice note received over WhatsApp from a rural woman.
    Processes the transcript using RAG, determines matching schemes,
    and returns a spoken audio note in her mother tongue.
    """
    transcript = req.audio_transcript.lower()
    is_pregnant = any(w in transcript for w in ["bacha", "garbh", "pregnant", "delivery", "prasavam", "thaimai", "biddalu", "prasavam"])
    is_shg = any(w in transcript for w in ["shg", "samuh", "didi", "group", "kudumbashree", "sangam", "dwacra"])
    has_daughter = any(w in transcript for w in ["beti", "ladki", "daughter", "magal", "aadapilla", "makal"])
    is_gas = any(w in transcript for w in ["gas", "chulha", "cylinder", "aduppu"])

    matched = search_schemes(
        is_pregnant_lactating=is_pregnant,
        is_shg_member=is_shg,
        has_girl_child=has_daughter
    )

    primary = matched[0] if matched else None
    scheme_title = primary["vernacular_names"].get(req.language, primary["name"]) if primary else "सरकारी योजना"
    benefit = primary.get("benefit_amount", "वित्तीय मदद") if primary else "सहायता राशि"

    # Generate spoken voice note reply
    replies = {
        "hi": f"राम राम दीदी! हमने आपकी आवाज सुनी। आपके लिए सबसे अच्छी योजना है: {scheme_title}। इसमें आपको {benefit} सीधे बैंक में मिलेंगे। कागज के लिए सिर्फ आधार कार्ड और बैंक पासबुक चाहिए। अगर मदद चाहिए तो 'दीदी' बोलकर ऑडियो भेजें!",
        "ta": f"வணக்கம் சகோதரி! உங்கள் குரல் பதிவு கிடைத்தது. உங்களுக்கு உகந்த திட்டம்: {scheme_title}. இதில் {benefit} நேரடியாக வங்கி கணக்கில் கிடைக்கும். தேவைப்படும் ஆவணம்: ஆதார் மற்றும் வங்கி பாஸ்புக்.",
        "te": f"నమస్కారం అక్కా! మీ వాయిస్ మెసేజ్ అందింది. మీ కోసం ఉత్తమ పథకం: {scheme_title}. దీని ద్వారా {benefit} అందుతాయి. అవసరమైన కాగితాలు: ఆధార్ కార్డు మరియు బ్యాంక్ పాస్ బుక్.",
        "ml": f"നമസ്കാരം സഹോദരീ! നിങ്ങളുടെ ശബ്ദ സന്ദേശം കേട്ടു. ഏറ്റവും അനുയോജ്യമായ പദ്ധതി: {scheme_title}. ഇതിലൂടെ {benefit} ലഭ്യമാണ്. ആധാർ കാർഡും ബാങ്ക് പാസ്സ്ബുക്കും കരുതുക."
    }
    audio_reply = replies.get(req.language, replies["hi"])

    return {
        "status": "success",
        "sender": req.caller_phone,
        "input_transcript": req.audio_transcript,
        "detected_intent": {
            "maternal": is_pregnant,
            "shg": is_shg,
            "daughter": has_daughter,
            "gas": is_gas
        },
        "matched_schemes": matched[:3],
        "reply_audio_text": audio_reply,
        "assigned_worker": "Sunita Devi (SHG Bank Sakhi, Contact: 98765-43210)"
    }

# Conversational Agent Endpoints
class AgentInteractRequest(BaseModel):
    user_speech: str
    language: str = "hi"
    dialect: Optional[str] = "standard"
    session_id: Optional[str] = "conv-1"

@app.post("/api/agent/interact")
def interact_with_agent(req: AgentInteractRequest):
    """
    Live conversational AI interface: listens to person's natural speech,
    understands rural welfare needs, and speaks back in their mother tongue.
    """
    from backend.conversational_agent import respond_to_human
    result = respond_to_human(
        user_speech=req.user_speech,
        language=req.language,
        dialect=req.dialect or "standard"
    )
    return {
        "status": "success",
        "user_speech": req.user_speech,
        "language": req.language,
        **result
    }

# Human Fallback Queue Endpoints
@app.get("/api/fallback/queue")
def list_fallback_queue():
    return {"status": "success", "tickets": get_fallback_queue()}

@app.post("/api/fallback/update")
def update_fallback_ticket(req: TicketUpdateRequest):
    success = update_ticket_status(req.ticket_id, req.status, req.notes)
    if not success:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"status": "success", "ticket_id": req.ticket_id, "new_status": req.status}

# Static files for frontend
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
def serve_index():
    index_file = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "VoiceSetu Backend is running. Frontend index.html not found."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
