"""
VoiceSetu Dialogue Engine - Audio-First IVR State Machine for Zero-Literacy Rural Women
Enforces:
1. Every step spoken aloud; DTMF keypad (1=Yes, 2=No, 9=Repeat, *=Discreet Panic) or voice confirmation.
2. Spoken Consent and Audio Verification.
3. Multi-language support: Hindi, Tamil, Telugu, Malayalam, with dialect nuances.
4. Confidence-based evaluation and one-button escalation to human SHG/CSC worker.
"""

from typing import Dict, Any, Optional
import uuid
from backend.schemes_rag import search_schemes, get_scheme_by_id

# Native audio dialogue prompts for each language and step
LOCALIZED_PROMPTS = {
    "hi": {
        "greeting_consent": "नमस्ते दीदी! यह भारत सरकार और राज्य सरकार की ग्रामीण महिलाओं की सरकारी योजनाओं की बोलती हुई फोन सेवा है। आगे बढ़ने के लिए आपकी सहमति चाहिए। अगर आप सहमत हैं, तो फोन पर 1 दबाइए या 'हाँ' बोलिए। बंद करने के लिए 2 दबाइए।",
        "repeat_hint": "दोबारा सुनने के लिए 9 दबाइए। किसी भी समय गुप्त मौसम रिपोर्ट के लिए स्टार (*) दबाइए।",
        "lang_confirm": "आपने हिंदी भाषा चुनी है। क्या आप भोजपुरी या बुंदेली लहजे में सुनना चाहती हैं? सामान्य हिंदी के लिए 1, देहाती लहजे के लिए 2 दबाइए।",
        "q_pregnant": "दीदी, क्या आप अभी गर्भवती हैं या आपकी गोद में छोटा बच्चा है? हाँ के लिए 1 दबाइए या 'हाँ' बोलिए, नहीं के लिए 2 दबाइए।",
        "q_shg": "क्या आप गांव के किसी स्वयं सहायता समूह यानी दीदी समूह (SHG / आजीविका मिशन) से जुड़ी हैं? हाँ के लिए 1 दबाइए, नहीं के लिए 2 दबाइए।",
        "q_daughter": "क्या आपके परिवार में 10 साल से छोटी बिटिया या स्कूल जाने वाली बेटी है? हाँ के लिए 1 दबाइए, नहीं के लिए 2 दबाइए।",
        "q_ration": "क्या आपके पास बीपीएल, पीला या अंत्योदय राशन कार्ड है? हाँ के लिए 1, नहीं के लिए 2 दबाइए।",
        "evaluating": "आपकी बातें सुनकर सरकारी नियमों के अनुसार सबसे लाभकारी योजनाएं खोजी जा रही हैं... कृपया 5 सेकंड प्रतीक्षा करें।",
        "results_found": "बधाई हो दीदी! आपकी बातों के आधार पर आप {count} प्रमुख योजनाओं के लिए पूरी तरह पात्र हैं। सबसे पहली योजना है: {scheme_name}। इसमें आपको {benefit} मिलेंगे।",
        "doc_checklist": "कागजात की बोलती सूची: पहला, अपना आधार कार्ड। दूसरा, बैंक पासबुक जिसमें सरकारी पैसा (DBT) चालू हो। तीसरा, राशन कार्ड। क्या ये तीनों कागज आपके पास घर पर हैं? हाँ के लिए 1 दबाइए, यदि कोई कागज कम है तो 2 दबाइए।",
        "token_scheduled": "आपका टोकन नंबर {token} बन गया है। कल सुबह 10 बजे आपके गांव के पंचायत भवन में बैंक सखी दीदी से मिलें। फोन पर निशुल्क ऑडियो पर्ची भेज दी गई है।",
        "fallback_reassure": "दीदी, बिल्कुल चिंता मत कीजिए! आपकी आवाज स्पष्ट नहीं आई या कागज समझने में दिक्कत है। हम आपकी फोन कॉल तुरंत आपके गांव की बैंक सखी सुनीता दीदी से जोड़ रहे हैं। कृपया लाइन पर बने रहें...",
        "panic_camouflage": "आज का मौसम: क्षेत्र में हल्की धूप रहेगी, शाम को ठंडी हवाएं चलेंगी। धान और गेहूं की फसल में हल्की सिंचाई करें।"
    },
    "ta": {
        "greeting_consent": "வணக்கம் சகோதரி! இது கிராமப்புற பெண்களுக்கான அரசு நலத்திட்டங்களை குரல் வழியே அறியும் தொலைபேசி சேவை. உங்கள் அனுமதியுடன் தொடங்க விரும்புகிறோம். சம்மதம் என்றால் 1-ஐ அழுத்தவும் அல்லது 'ஆம்' என்று கூறவும். இணைப்பை துண்டிக்க 2-ஐ அழுத்தவும்.",
        "repeat_hint": "மீண்டும் கேட்க 9-ஐ அழுத்தவும். அவசர மறைப்புக்கு ஸ்டார் (*) அழுத்தவும்.",
        "lang_confirm": "நீங்கள் தமிழ் மொழியை தேர்வு செய்துள்ளீர்கள்.",
        "q_pregnant": "சகோதரி, நீங்கள் தற்போது கர்ப்பமாக இருக்கிறீர்களா அல்லது பாலூட்டும் தாயா? ஆம் என்றால் 1-ஐ அழுத்தவும், இல்லை என்றால் 2-ஐ அழுத்தவும்.",
        "q_shg": "நீங்கள் கிராம சுயஉதவி குழுவில் (SHG) உறுப்பினராக உள்ளீர்களா? ஆம் என்றால் 1-ஐ அழுத்தவும், இல்லை என்றால் 2-ஐ அழுத்தவும்.",
        "q_daughter": "உங்கள் குடும்பத்தில் 10 வயதுக்குட்பட்ட பெண் குழந்தை அல்லது பள்ளி செல்லும் மகள் உள்ளாரா? ஆம் என்றால் 1, இல்லை என்றால் 2.",
        "q_ration": "உங்களிடம் குடும்ப அட்டை (ரேஷன் கார்டு) உள்ளதா? ஆம் என்றால் 1, இல்லை என்றால் 2 அழுத்தவும்.",
        "evaluating": "உங்கள் பதில்களை கொண்டு அரசு விதிகளின்படி சரியான திட்டங்கள் கண்டறியப்படுகின்றன... காத்திருக்கவும்.",
        "results_found": "வாழ்த்துக்கள் சகோதரி! உங்கள் விவரங்களின்படி நீங்கள் {count} முக்கிய திட்டங்களுக்கு தகுதியானவர். முதல் திட்டம்: {scheme_name}. இதில் உங்களுக்கு {benefit} கிடைக்கும்.",
        "doc_checklist": "தேவையான ஆவணங்கள்: உங்கள் ஆதார் அட்டை, ஆதாருடன் இணைக்கப்பட்ட வங்கி கணக்கு புத்தகம், மற்றும் குடும்ப அட்டை. இவற்றுடன் தயாராக உள்ளீர்களா? ஆம் என்றால் 1, உதவி தேவை என்றால் 2 அழுத்தவும்.",
        "token_scheduled": "உங்கள் டோக்கன் எண் {token}. கிராம ஊராட்சி சேவை மையத்தில் உதவி பெறலாம். உங்கள் செல்போனுக்கு ஆடியோ தகவல் அனுப்பப்பட்டுள்ளது.",
        "fallback_reassure": "கவலைப்பட வேண்டாம் சகோதரி! உங்கள் அழைப்பை உடனடியாக உங்கள் பகுதி கிராம சேவை மைய மகளிர் அலுவலருக்கு இணைக்கிறோம். தொடர்பிலேயே இருங்கள்...",
        "panic_camouflage": "இன்றைய வானிலை அறிக்கை: உங்கள் பகுதியில் மிதமான வெயிலும் மாலையில் இதமான காற்றும் வீசும். நெல் பயிர்களுக்கு தகுந்த நீர்ப்பாசனம் செய்யவும்."
    },
    "te": {
        "greeting_consent": "నమస్కారం అక్కా! ఇది గ్రామీణ మహిళల ప్రభుత్వ సంక్షేమ పథకాలను ఫోన్ ద్వారా తెలియజేసే వాయిస్ సేవ. కొనసాగించడానికి మీ అనుమతి కావాలి. సమ్మతమైతే 1 నొక్కండి లేదా 'అవును' అని చెప్పండి. ముగించడానికి 2 నొక్కండి.",
        "repeat_hint": "మళ్లీ వినడానికి 9 నొక్కండి. ప్రైవసీ మోడ్ కోసం స్టార్ (*) నొక్కండి.",
        "lang_confirm": "మీరు తెలుగు భాషను ఎంచుకున్నారు.",
        "q_pregnant": "అక్కా, మీరు ప్రస్తుతం గర్భిణీలా లేదా చంటిపిల్లల తల్లినా? అవును అయితే 1 నొక్కండి, కాకపోతే 2 నొక్కండి.",
        "q_shg": "మీరు గ్రామంలోని డ్వాక్రా మహిళా సంఘంలో (SHG) సభ్యురాలా? అవును అయితే 1, కాకపోతే 2 నొక్కండి.",
        "q_daughter": "మీ ఇంట్లో 10 ఏళ్లలోపు ఆడపిల్ల లేదా చదువుకునే కుమార్తె ఉన్నారా? అవును అయితే 1, కాకపోతే 2 నొక్కండి.",
        "q_ration": "మీకు తెల్ల రేషన్ కార్డు లేదా రైస్ కార్డు ఉందా? అవును అయితే 1, కాకపోతే 2 నొక్కండి.",
        "evaluating": "మీ వివరాల ఆధారంగా ప్రభుత్వ నియమాలను సరిచూస్తున్నాము... దయచేసి వేచి ఉండండి.",
        "results_found": "శుభవార్త అక్కా! మీరు {count} ముఖ్యమైన పథకాలకు అర్హులు. ప్రధాన పథకం: {scheme_name}. దీని ద్వారా మీకు {benefit} లభిస్తుంది.",
        "doc_checklist": "కావాల్సిన కాగితాలు: మీ ఆధార్ కార్డు, బ్యాంకు పాస్ బుక్ (DBT లింక్ అయినది), మరియు రేషన్ కార్డు. ఇవి సిద్ధంగా ఉంటే 1 నొక్కండి, సాయం కావాలంటే 2 నొక్కండి.",
        "token_scheduled": "మీ టోకెన్ నెంబర్ {token} ఖరారైంది. రేపు గ్రామ సచివాలయంలో మహిళా సహాయకురాలిని కలవండి. వాయిస్ మెసేజ్ పంపబడింది.",
        "fallback_reassure": "ఆందోళన చెందవద్దు అక్కా! మీ కాల్‌ను వెంటనే మీ గ్రామ సచివాలయ మహిళా మిత్రతో కలుపుతున్నాము. దయచేసి లైన్లోనే ఉండండి...",
        "panic_camouflage": "నేటి వాతావరణం: ఆకాశం నిర్మలంగా ఉంటుంది. వ్యవసాయ పంటలకు నీటి పారుదల సక్రమంగా చేయండి."
    },
    "ml": {
        "greeting_consent": "നമസ്കാരം സഹോദരീ! ഗ്രാമീണ സ്ത്രീകൾക്കായുള്ള സർക്കാർ ക്ഷേമപദ്ധതികൾ ഫോൺ വഴി സംസാരിച്ച് പറഞ്ഞുതരുന്ന സേവനമാണിത്. ആരംഭിക്കാൻ സമ്മതമെങ്കിൽ 1 അമർത്തുക അല്ലെങ്കിൽ 'ഉണ്ട്' എന്ന് പറയുക. അവസാനിപ്പിക്കാൻ 2 അമർത്തുക.",
        "repeat_hint": "വീണ്ടും കേൾക്കാൻ 9 അമർത്തുക. പെട്ടെന്ന് കാലാവസ്ഥ റിപ്പോർട്ടിലേക്ക് മാറ്റാൻ സ്റ്റാർ (*) അമർത്തുക.",
        "lang_confirm": "നിങ്ങൾ മലയാളം ഭാഷ തെരഞ്ഞെടുത്തു.",
        "q_pregnant": "സഹോദരീ, നിങ്ങൾ ഇപ്പോൾ ഗർഭിണിയോ അല്ലെങ്കിൽ മുലയൂട്ടുന്ന അമ്മയോ ആണോ? ആണെങ്കിൽ 1 അമർത്തുക, അല്ലെങ്കില്‍ 2 അമർത്തുക.",
        "q_shg": "നിങ്ങൾ കുടുംബശ്രീ അല്ലെങ്കിൽ ഏതെങ്കിലും അയൽക്കൂട്ട സ്വയംസഹായ സംഘത്തിൽ അംഗമാണോ? ആണെങ്കിൽ 1, അല്ലെങ്കില്‍ 2 അമർത്തുക.",
        "q_daughter": "നിങ്ങളുടെ കുടുംബത്തിൽ 10 വയസ്സിൽ താഴെയുള്ള പെൺകുട്ടിയോ പഠിക്കുന്ന മകളോ ഉണ്ടോ? ആണെങ്കിൽ 1, അല്ലെങ്കില്‍ 2 അമർത്തുക.",
        "q_ration": "നിങ്ങൾക്ക് റേഷൻ കാർഡ് ഉണ്ടോ? ഉണ്ടെങ്കിൽ 1, ഇല്ലെങ്കിൽ 2 അമർത്തുക.",
        "evaluating": "സർക്കാർ മാനദണ്ഡങ്ങൾ പരിശോധിച്ച് അർഹമായ പദ്ധതികൾ കണ്ടെത്തുന്നു... കാത്തിരിക്കുക.",
        "results_found": "സന്തോഷവാർത്ത സഹോദരീ! നിങ്ങൾക്ക് {count} പ്രധാന പദ്ധതികളിലേക്ക് അർഹതയുണ്ട്. പ്രധാന പദ്ധതി: {scheme_name}. ഇതിലൂടെ നിങ്ങൾക്ക് {benefit} ലഭിക്കും.",
        "doc_checklist": "ആവശ്യമായ രേഖകൾ: ആധാർ കാർഡ്, ഡിബിടി സൗകര്യമുള്ള ബാങ്ക് പാസ്സ്ബുക്ക്, റേഷൻ കാർഡ്. ഇവ കൈവശമുണ്ടെങ്കിൽ 1 അമർത്തുക, സഹായം വേണമെങ്കിൽ 2 അമർത്തുക.",
        "token_scheduled": "നിങ്ങളുടെ ടോക്കൺ നമ്പർ {token}. ഗ്രാമപഞ്ചായത്ത് കുടുംബശ്രീ സിഡിഎസ് ഓഫീസിൽ നിന്ന് സേവനം ലഭിക്കും.",
        "fallback_reassure": "വിഷമിക്കേണ്ട സഹോദരീ! നിങ്ങളുടെ കോൾ ഉടൻ തന്നെ കുടുംബശ്രീ പ്രതിനിധിയിലേക്ക് ബന്ധിപ്പിക്കുന്നു. ദയവായി കാത്തിരിക്കുക...",
        "panic_camouflage": "ഇന്നത്തെ കാലാവസ്ഥ: പകൽ തെളിഞ്ഞ കാലാവസ്ഥയും വൈകുന്നേരം നേരിയ തണുത്ത കാറ്റും പ്രതീക്ഷിക്കാം."
    }
}

class IVRSession:
    def __init__(self, session_id: str, lang: str = "hi", dialect: str = "standard"):
        self.session_id = session_id
        self.lang = lang if lang in LOCALIZED_PROMPTS else "hi"
        self.dialect = dialect
        self.state = "GREETING_CONSENT"
        self.user_answers: Dict[str, Any] = {
            "is_pregnant_lactating": False,
            "is_shg_member": False,
            "has_girl_child": False,
            "has_ration_card": True,
            "marital_status": "married"
        }
        self.matched_schemes = []
        self.confidence_score = 0.95
        self.escalated = False
        self.history = []

    def get_prompt(self, key: str, **kwargs) -> str:
        lang_dict = LOCALIZED_PROMPTS.get(self.lang, LOCALIZED_PROMPTS["hi"])
        template = lang_dict.get(key, LOCALIZED_PROMPTS["hi"].get(key, ""))
        return template.format(**kwargs)

    def process_input(self, user_input: str, ambient_noise_db: float = 30.0) -> Dict[str, Any]:
        """
        Processes DTMF button or voice text. Evaluates ambient noise and confidence.
        """
        clean_input = user_input.strip().lower()

        # Check for Panic / Quick hangup code
        if clean_input in ["*", "star", "panic", "mausam", "weather", "rasoi", "hangup"]:
            return {
                "action": "CAMOUFLAGE",
                "audio_text": self.get_prompt("panic_camouflage"),
                "status": "safe_mode",
                "screen_state": "WEATHER_REPORT"
            }

        # Check for Human escalation explicit request
        if any(w in clean_input in clean_input for w in ["didi", "sakhi", "help", "officer", "insaan", "manithan", "sahayam", "help me", "talk to human", "agent"]):
            self.escalated = True
            return {
                "action": "ESCALATE_HUMAN",
                "audio_text": self.get_prompt("fallback_reassure"),
                "reason": "Explicit user request for human SHG worker",
                "status": "connecting_shg_didi"
            }

        # Ambient noise adjustment: high noise (>65dB) lowers confidence
        if ambient_noise_db > 65:
            self.confidence_score = max(0.40, 1.0 - (ambient_noise_db - 50) / 100)
            if self.confidence_score < 0.65:
                self.escalated = True
                return {
                    "action": "ESCALATE_HUMAN",
                    "audio_text": self.get_prompt("fallback_reassure"),
                    "reason": f"High ambient noise ({ambient_noise_db:.1f} dB) resulting in low confidence ({self.confidence_score:.2f})",
                    "status": "connecting_shg_didi"
                }

        # Repeat prompt command
        if clean_input in ["9", "repeat", "phir se", "thirumba"]:
            return self.current_step_response()

        # State Machine Transitions
        if self.state == "GREETING_CONSENT":
            if clean_input in ["1", "haan", "yes", "aam", "avunu", "und", "agree"]:
                self.state = "Q_PREGNANT"
                return {
                    "state": self.state,
                    "audio_text": self.get_prompt("q_pregnant"),
                    "dtmf_options": [{"key": "1", "label": "Haan / Yes"}, {"key": "2", "label": "Nahin / No"}]
                }
            elif clean_input in ["2", "nahi", "no", "illai", "kaadhu", "illa"]:
                return {
                    "state": "CALL_TERMINATED",
                    "audio_text": "धन्यवाद दीदी। आपकी अनुमति के बिना कोई जानकारी एकत्र नहीं की गई है। नमस्ते।",
                    "action": "END_CALL"
                }
            else:
                return {
                    "state": self.state,
                    "audio_text": "कृपया सहमति के लिए 1 दबाएं या 'हाँ' बोलें। बंद करने के लिए 2 दबाएं।",
                    "dtmf_options": [{"key": "1", "label": "1: Haan"}, {"key": "2", "label": "2: Nahin"}]
                }

        elif self.state == "Q_PREGNANT":
            self.user_answers["is_pregnant_lactating"] = (clean_input in ["1", "haan", "yes", "aam", "avunu", "und"])
            self.state = "Q_SHG"
            return {
                "state": self.state,
                "audio_text": self.get_prompt("q_shg"),
                "dtmf_options": [{"key": "1", "label": "1: SHG Member"}, {"key": "2", "label": "2: Not Member"}]
            }

        elif self.state == "Q_SHG":
            self.user_answers["is_shg_member"] = (clean_input in ["1", "haan", "yes", "aam", "avunu", "und"])
            self.state = "Q_DAUGHTER"
            return {
                "state": self.state,
                "audio_text": self.get_prompt("q_daughter"),
                "dtmf_options": [{"key": "1", "label": "1: Girl Child in Family"}, {"key": "2", "label": "2: No"}]
            }

        elif self.state == "Q_DAUGHTER":
            self.user_answers["has_girl_child"] = (clean_input in ["1", "haan", "yes", "aam", "avunu", "und"])
            self.state = "Q_RATION"
            return {
                "state": self.state,
                "audio_text": self.get_prompt("q_ration"),
                "dtmf_options": [{"key": "1", "label": "1: Have Ration Card"}, {"key": "2", "label": "2: No Card"}]
            }

        elif self.state == "Q_RATION":
            self.user_answers["has_ration_card"] = (clean_input in ["1", "haan", "yes", "aam", "avunu", "und"])
            # Run RAG rules engine
            matched = search_schemes(
                marital_status=self.user_answers["marital_status"],
                has_girl_child=self.user_answers["has_girl_child"],
                is_shg_member=self.user_answers["is_shg_member"],
                is_pregnant_lactating=self.user_answers["is_pregnant_lactating"]
            )
            self.matched_schemes = matched
            primary = matched[0] if matched else None
            scheme_title = primary["vernacular_names"].get(self.lang, primary["name"]) if primary else "महिला कल्याण योजना"
            benefit = primary.get("benefit_amount", "वित्तीय लाभ") if primary else "योजना लाभ"

            self.state = "RESULTS_AND_DOCS"
            results_text = self.get_prompt("results_found", count=len(matched), scheme_name=scheme_title, benefit=benefit)
            checklist_text = self.get_prompt("doc_checklist")

            return {
                "state": self.state,
                "audio_text": f"{results_text} {checklist_text}",
                "matched_schemes": matched,
                "dtmf_options": [{"key": "1", "label": "1: Have All Docs"}, {"key": "2", "label": "2: Need Help / Missing Docs"}]
            }

        elif self.state == "RESULTS_AND_DOCS":
            if clean_input in ["1", "haan", "yes", "aam", "avunu", "und"]:
                # Generates token and offline guidance
                token_code = f"VS-{str(uuid.uuid4())[:6].upper()}"
                self.state = "TOKEN_CONFIRMED"
                confirmation_text = self.get_prompt("token_scheduled", token=token_code)
                return {
                    "state": self.state,
                    "audio_text": confirmation_text,
                    "token_number": token_code,
                    "action": "SCHEDULED_OFFLINE_VISIT"
                }
            else:
                # Missing documents - escalate to SHG worker for physical doorstep verification
                self.escalated = True
                return {
                    "action": "ESCALATE_HUMAN",
                    "audio_text": self.get_prompt("fallback_reassure"),
                    "reason": "Missing documents - Doorstep physical paperwork assistance required",
                    "status": "connecting_shg_didi"
                }

        elif self.state == "TOKEN_CONFIRMED":
            return {
                "state": "COMPLETED",
                "audio_text": "धन्यवाद दीदी! आपकी ऑडियो पर्ची सुरक्षित है। शुभ दिन।",
                "action": "CALL_DONE"
            }

        return self.current_step_response()

    def current_step_response(self) -> Dict[str, Any]:
        """Repeats current step audio."""
        if self.state == "GREETING_CONSENT":
            return {"state": self.state, "audio_text": self.get_prompt("greeting_consent")}
        elif self.state == "Q_PREGNANT":
            return {"state": self.state, "audio_text": self.get_prompt("q_pregnant")}
        elif self.state == "Q_SHG":
            return {"state": self.state, "audio_text": self.get_prompt("q_shg")}
        elif self.state == "Q_DAUGHTER":
            return {"state": self.state, "audio_text": self.get_prompt("q_daughter")}
        elif self.state == "Q_RATION":
            return {"state": self.state, "audio_text": self.get_prompt("q_ration")}
        elif self.state == "RESULTS_AND_DOCS":
            return {"state": self.state, "audio_text": self.get_prompt("doc_checklist")}
        return {"state": self.state, "audio_text": "हम आपकी सहायता के लिए तैयार हैं।"}

# Active IVR sessions memory
_active_sessions: Dict[str, IVRSession] = {}

def get_or_create_session(session_id: Optional[str] = None, lang: str = "hi", dialect: str = "standard") -> IVRSession:
    if not session_id or session_id not in _active_sessions:
        new_id = session_id or str(uuid.uuid4())
        _active_sessions[new_id] = IVRSession(session_id=new_id, lang=lang, dialect=dialect)
    else:
        # If user changed language, update it
        if lang in LOCALIZED_PROMPTS:
            _active_sessions[session_id].lang = lang
            _active_sessions[session_id].dialect = dialect
    return _active_sessions[new_id if not session_id else session_id]
