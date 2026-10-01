"""
VoiceSetu Safety & Privacy Camouflage Engine
Enables discreet use for rural women facing domestic surveillance or social risks.
Provides instant camouflage screen and audio:
- Weather Advisory ("Mausam Samachar")
- Cooking Recipe ("Desi Rasoi")
- Wipes or cloaks temporary voice inquiry logs.
"""

from typing import Dict, Any

CAMOUFLAGE_DATA = {
    "weather": {
        "title": {
            "hi": "दैनिक ग्रामीण मौसम एवं फसल सलाह",
            "ta": "தினசரி வானிலை மற்றும் வேளாண் அறிக்கை",
            "te": "రోజువారీ వాతావరణ మరియు పంట సలహా",
            "ml": "ദൈനംദിന കാലാവസ്ഥാ കാർഷിക വിവരങ്ങൾ",
            "en": "Daily Rural Weather & Crop Advisory"
        },
        "audio_text": {
            "hi": "नमस्कार किसान भाई-बहनों! आज आपके इलाके में मौसम साफ रहेगा। दोपहर में हल्की धूप और शाम को ठंडी हवाएं चलेंगी। गेहूं और सरसों की फसल में हल्की सिंचाई करने की सलाह दी जाती है।",
            "ta": "வணக்கம்! இன்று உங்கள் பகுதியில் வானிலை சீராக இருக்கும். மாலையில் மிதமான காற்று வீசும். நெற்பயிர்களுக்கு தகுந்த நீர்ப்பாசனம் செய்யவும்.",
            "te": "నమస్కారం! నేడు మీ ప్రాంతంలో వాతావరణం పొడిగా ఉంటుంది. సాయంత్రం చల్లని గాలులు వీస్తాయి. వరి పంటకు తగినంత నీటి పారుదల చేయండి.",
            "ml": "നമസ്കാരം! ഇന്ന് നിങ്ങളുടെ പ്രദേശത്ത് തെളിഞ്ഞ കാലാവസ്ഥയായിരിക്കും. കൃഷിയിടങ്ങളിൽ നേരിയ നനവ് നൽകുന്നത് നല്ലതാണ്.",
            "en": "Weather update: Clear skies expected with gentle breeze in the evening. Recommended to irrigate crops as per seasonal guidelines."
        },
        "visual_metrics": {
            "temperature": "29°C",
            "humidity": "54%",
            "wind": "12 km/h NE",
            "crop_tip": "Apply organic neem spray for pest control"
        }
    },
    "recipe": {
        "title": {
            "hi": "पारंपरिक देसी रसोई - दाल तड़का व बाजरा रोटी",
            "ta": "பாரம்பரிய சமையல் குறிப்பு - பருப்பு ரசம்",
            "te": "సాంప్రదాయ వంటకాలు - పప్పు చారు",
            "ml": "നാടൻ പാചകക്കുറിപ്പ് - പരിപ്പ് കറി",
            "en": "Traditional Kitchen Recipes"
        },
        "audio_text": {
            "hi": "नमस्ते! आज की आसान रेसिपी है स्वादिष्ट तूर दाल तड़का। दाल को धोकर कुकर में तीन सीटी लगाएं। घी में जीरा, हींग और सूखी लाल मिर्च का छौंक लगाएं।",
            "ta": "வணக்கம்! இன்றைய எளிய சமையல் பருப்பு ரசம். நெய்யில் சீரகம், பெருங்காயம் தாளித்து சூடான சாதத்துடன் பரிமாறவும்.",
            "te": "నమస్కారం! నేటి వంటకం కమ్మని పప్పు చారు. నేతిలో జీలకర్ర, ఇంగువ పోపు వేసి వేడివేడిగా సర్వ్ చేయండి.",
            "ml": "നമസ്കാരം! ഇന്നത്തെ വിഭവം രുചികരമായ പരിപ്പ് കറിയാണ്. കടുക്, വറ്റൽമുളക് താളിച്ച് ചൂടോടെ വിളമ്പാം.",
            "en": "Today's traditional recipe: Wholesome lentil curry tempered with cumin and ghee."
        }
    }
}

def get_camouflage_payload(mode: str = "weather", lang: str = "hi") -> Dict[str, Any]:
    selected_mode = CAMOUFLAGE_DATA.get(mode, CAMOUFLAGE_DATA["weather"])
    return {
        "is_camouflaged": True,
        "mode": mode,
        "screen_title": selected_mode["title"].get(lang, selected_mode["title"]["en"]),
        "audio_script": selected_mode["audio_text"].get(lang, selected_mode["audio_text"]["en"]),
        "visual_details": selected_mode.get("visual_metrics", {})
    }
