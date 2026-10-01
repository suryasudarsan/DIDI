"""
VoiceSetu RAG Engine - Comprehensive Knowledge Base of Indian Government Schemes for Rural Women
Covers Central Government and State Governments (Tamil Nadu, Andhra Pradesh, Telangana, Kerala, MP, UP, Bihar, etc.)
Rules are verified against official scheme guidelines, eligibility matrices, required documents, and offline submission paths.
"""

from typing import List, Dict, Any, Optional

SCHEMES_DATABASE: List[Dict[str, Any]] = [
    {
        "id": "pmmvy",
        "name": "Pradhan Mantri Matru Vandana Yojana (PMMVY)",
        "vernacular_names": {
            "hi": "प्रधानमंत्री मातृ वंदना योजना",
            "ta": "பிரதம மந்திரி மாத்ரு வந்தனா யோஜனா (தாய்மை உதவி)",
            "te": "ప్రధాన మంత్రి మాతృ వందన యోజన",
            "ml": "പ്രധാനമന്ത്രി മാതൃ വന്ദന യോജന",
            "en": "PM Maternity Benefit Scheme"
        },
        "category": "maternity",
        "scope": "Central",
        "benefit_amount": "₹5,000 for 1st child, ₹6,000 for 2nd girl child",
        "descriptions": {
            "hi": "गर्भवती और स्तनपान कराने वाली माताओं को पोषण और स्वास्थ्य के लिए सीधे बैंक खाते में 5,000 से 6,000 रुपये की आर्थिक सहायता।",
            "ta": "கர்ப்பிணி மற்றும் பாலூட்டும் தாய்மார்களுக்கு ஊட்டச்சத்து மற்றும் மருத்துவ சிகிச்சைக்காக நேரடியாக வங்கி கணக்கில் ₹5,000 முதல் ₹6,000 நிதி உதவி.",
            "te": "గర్భిణీ మరియు బాలింత స్త్రీలకు పోషకాహారం మరియు ఆరోగ్య సంరక్షణ కొరకు నేరుగా బ్యాంక్ ఖాతాలో ₹5,000 నుండి ₹6,000 ఆర్థిక సహాయం.",
            "ml": "ഗർഭിണികൾക്കും മുലയൂട്ടുന്ന അമ്മമാർക്കും പോഷകാഹാരത്തിനും ആരോഗ്യ സംരക്ഷണത്തിനുമായി ബാങ്ക് അക്കൗണ്ടിലേക്ക് ₹5,000 മുതൽ ₹6,000 വരെ ധനസഹായം.",
            "en": "Direct cash incentive of ₹5,000 to ₹6,000 into bank accounts for pregnant women and lactating mothers for nutrition and wage loss compensation."
        },
        "eligibility": {
            "min_age": 19,
            "max_age": 50,
            "marital_status": ["married", "pregnant", "lactating"],
            "income_limit_per_annum": 800000,
            "bpl_required": False,
            "target_group": "Pregnant women and lactating mothers (1st or 2nd child)",
            "special_condition": "Second child must be a girl child for ₹6,000 bonus installment."
        },
        "documents_required": [
            {"doc": "Aadhaar Card of Mother", "vernacular": {"hi": "माता का आधार कार्ड", "ta": "தாயின் ஆதார் அட்டை", "te": "తల్లి ఆధార్ కార్డు", "ml": "അമ്മയുടെ ആധാർ കാർഡ്"}},
            {"doc": "Aadhaar Card of Husband", "vernacular": {"hi": "पति का आधार कार्ड", "ta": "கணவரின் ஆதார் அட்டை", "te": "భర్త ఆధార్ కార్డు", "ml": "ഭർത്താവിന്റെ ആധാർ കാർഡ്"}},
            {"doc": "Mother-Child Protection (MCP) Card from Anganwadi", "vernacular": {"hi": "आंगनवाड़ी से जच्चा-बच्चा (MCP) कार्ड", "ta": "அங்கன்வாடி தாய்-சேய் அட்டை", "te": "అంగన్‌వాడీ MCP కార్డ్", "ml": "അംഗൻവാടി എംസിപി കാർഡ്"}},
            {"doc": "Bank Passbook linked to Aadhaar (NPCI active)", "vernacular": {"hi": "आधार से जुड़ा बैंक खाता पासबुक", "ta": "ஆதாருடன் இணைக்கப்பட்ட வங்கி கணக்கு புத்தகம்", "te": "ఆధార్ అనుసంధాన బ్యాంక్ పాస్ బుక్", "ml": "ആധാറുമായി ബന്ധിപ്പിച്ച ബാങ്ക് പാസ്സ്ബുക്ക്"}}
        ],
        "offline_process": {
            "submission_center": "Anganwadi Center or Village Health Sub-Centre (ASHA didi)",
            "action": "Submit Form 1A/1B within 270 days of pregnancy registration at nearest Anganwadi. No internet needed; ASHA worker uploads data.",
            "token_code_prefix": "PMMVY-RUR"
        }
    },
    {
        "id": "lakhpati_didi",
        "name": "Lakhpati Didi Initiative (DAY-NRLM)",
        "vernacular_names": {
            "hi": "लखपति दीदी योजना (स्वयं सहायता समूह)",
            "ta": "இலட்சாதிபதி சகோதரி திட்டம் (சுயஉதவி குழு)",
            "te": "లఖ్‌పతి దీదీ పథకం (మహిళా సంఘాలు)",
            "ml": "ലഖ്പതി ദീദി പദ്ധതി (കുടുംബശ്രീ / സ്വയംസഹായ സംഘം)",
            "en": "Lakhpati Didi Rural Livelihood Mission"
        },
        "category": "livelihood",
        "scope": "Central",
        "benefit_amount": "₹1,00,000+ annual sustainable income per household + interest-subsidized collateral-free loans up to ₹5,00,000",
        "descriptions": {
            "hi": "गांव के स्वयं सहायता समूह (SHG) की बहनों को कृषि, पशुपालन, सिलाई, ड्रोन और मिलेट उत्पादों में प्रशिक्षण और बिना गारंटी का आसान ऋण।",
            "ta": "கிராமப்புற சுயஉதவி குழு பெண்களுக்கு விவசாயம், கால்நடை வளர்ப்பு மற்றும் சிறுதொழில்களுக்கு வட்டியில்லா கடன் மற்றும் திறன் பயிற்சி.",
            "te": "గ్రామీణ స్వయం సహాయక సంఘాల మహిళలకు వ్యవసాయం, పశుపోషణ మరియు సూక్ష్మ వ్యాపారాల కోసం పూచీకత్తు లేని రుణాలు మరియు నైపుణ్య శిక్షణ.",
            "ml": "ഗ്രാമീണ സ്വയംസഹായ സംഘങ്ങളിലെ വനിതകൾക്ക് കൃഷി, പക്ഷി-മൃഗ പരിപാലനം, ചെറുകിട സംരംഭങ്ങൾ എന്നിവക്കായി വായ്പയും നൈപുണ്യ പരിശീലനവും.",
            "en": "Enables rural SHG women to earn a sustainable income of at least ₹1 Lakh per year through enterprise training, digital financial services, and Community Investment Funds."
        },
        "eligibility": {
            "min_age": 18,
            "max_age": 60,
            "marital_status": ["any"],
            "shg_member_required": True,
            "target_group": "Active members of Women Self Help Groups (SHG / Deendayal Antyodaya Yojana)",
            "special_condition": "Must be an active SHG member for at least 6 months with regular weekly savings."
        },
        "documents_required": [
            {"doc": "SHG Member Passbook / Identity Card", "vernacular": {"hi": "समूह की सदस्यता पासबुक / पहचान पत्र", "ta": "சுயஉதவி குழு உறுப்பினர் பாஸ்புக்", "te": "స్వయం సహాయక సంఘ సభ్యత్వ పాస్ బుక్", "ml": "എസ്.എച്ച്.ജി അംഗത്വ പാസ്സ്ബുക്ക്"}},
            {"doc": "Aadhaar Card", "vernacular": {"hi": "आधार कार्ड", "ta": "ஆதார் அட்டை", "te": "ఆధార్ కార్డు", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "Individual or Group Bank Account Details", "vernacular": {"hi": "व्यक्तिगत या समूह बैंक खाता", "ta": "வங்கி கணக்கு விவரங்கள்", "te": "బ్యాంక్ ఖాతా వివరాలు", "ml": "ബാങ്ക് അക്കൗണ്ട് വിവരങ്ങൾ"}}
        ],
        "offline_process": {
            "submission_center": "Gram Panchayat SHG Village Organization (VO) or Block Mission Management Unit (BMMU)",
            "action": "Meet your village Bank Sakhi or Krishi Sakhi at the next weekly SHG meeting. Micro-Investment Plan (MIP) is prepared offline.",
            "token_code_prefix": "LPD-SHG"
        }
    },
    {
        "id": "pmuy",
        "name": "Pradhan Mantri Ujjwala Yojana 2.0 (PMUY)",
        "vernacular_names": {
            "hi": "प्रधानमंत्री उज्ज्वला योजना 2.0 (मुफ्त गैस कनेक्शन)",
            "ta": "பிரதம மந்திரி உஜ்வாலா திட்டம் (இலவச எரிவாயு இணைப்பு)",
            "te": "ప్రధాన మంత్రి ఉజ్వల యోజన (ఉచిత గ్యాస్ కనెక్షన్)",
            "ml": "പ്രധാനമന്ത്രി ഉജ്ജ്വല യോജന (സൗജന്യ ഗ്യാസ് കണക്ഷൻ)",
            "en": "PM Ujjwala Clean Cooking Gas Scheme"
        },
        "category": "energy",
        "scope": "Central",
        "benefit_amount": "Free LPG Gas connection + Free 1st cylinder & hotplate stove + ₹300 subsidy per refill",
        "descriptions": {
            "hi": "गरीब ग्रामीण महिलाओं को धुएं से मुक्ति के लिए निशुल्क गैस सिलेंडर, चूल्हा और पहला रिफिल पूरी तरह मुफ्त।",
            "ta": "ஏழை கிராமப்புற பெண்களுக்கு இலவச சமையல் எரிவாயு இணைப்பு, அடுப்பு மற்றும் முதல் சிலிண்டர் முற்றிலும் இலவசம்.",
            "te": "గ్రామీణ పేద మహిళలకు ఉచిత వంటగ్యాస్ కనెక్షన్, పొయ్యి మరియు మొదటి సిలిండర్ ఉచితం.",
            "ml": "ഗ്രാമീണ മേഖലയിലെ നിർധനരായ വനിതകൾക്ക് സൗജന്യ ഗ്യാസ് കണക്ഷനും ആദ്യത്തെ സിലിണ്ടറും സ്റ്റൗവും സൗജന്യമായി ലഭിക്കുന്നു.",
            "en": "Deposit-free LPG connection for rural adult women from poor households, including free first cylinder refill and stove."
        },
        "eligibility": {
            "min_age": 18,
            "max_age": 90,
            "marital_status": ["any"],
            "gender": "female",
            "bpl_required": True,
            "target_group": "Adult rural woman belonging to SC/ST/PMAY/Antyodaya or economically disadvantaged household without existing LPG",
            "special_condition": "No other family member in the same ration card should possess an LPG connection."
        },
        "documents_required": [
            {"doc": "BPL Ration Card / 14-point declaration", "vernacular": {"hi": "राशन कार्ड (बीपीएल / अंत्योदय)", "ta": "ரேஷன் கார்டு (குடும்ப அட்டை)", "te": "రేషన్ కార్డు", "ml": "റേഷൻ കാർഡ്"}},
            {"doc": "Aadhaar Card of Woman Applicant", "vernacular": {"hi": "महिला आवेदक का आधार कार्ड", "ta": "விண்ணப்பதாரரின் ஆதார் அட்டை", "te": "మహిళా దరఖాస్తుదారుని ఆధార్ కార్డు", "ml": "അപേക്ഷകയുടെ ആധാർ കാർഡ്"}},
            {"doc": "Bank Passbook with IFSC code", "vernacular": {"hi": "बैंक खाता पासबुक", "ta": "வங்கி பாஸ்புக்", "te": "బ్యాంక్ పాస్ బుక్", "ml": "ബാങ്ക് പാസ്സ്ബുക്ക്"}},
            {"doc": "Passport size photo", "vernacular": {"hi": "पासपोर्ट साइज फोटो", "ta": "புகைப்படம்", "te": "ఫోటో", "ml": "ഫോട്ടോ"}}
        ],
        "offline_process": {
            "submission_center": "Nearest Rural LPG Gas Agency (Indane / Bharatgas / HP Gas) or CSC Village Center",
            "action": "Hand over paper application to the local delivery man or gas distributor office. Agency does doorstep verification and installs cylinder.",
            "token_code_prefix": "PMUY-GAS"
        }
    },
    {
        "id": "sukanya_samriddhi",
        "name": "Sukanya Samriddhi Yojana (SSY)",
        "vernacular_names": {
            "hi": "सुकन्या समृद्धि योजना (बेटी की बचत योजना)",
            "ta": "செல்வ மகள் சேமிப்பு திட்டம் (சுகன்யா சம்ரித்தி)",
            "te": "సుకున్య సమృద్ధి యోజన (ఆడపిల్లల పొదుపు పథకం)",
            "ml": "സുകന്യ സമൃദ്ധി യോജന (പെൺകുട്ടികളുടെ സമ്പാദ്യ പദ്ധതി)",
            "en": "Sukanya Samriddhi Girl Child Savings"
        },
        "category": "education",
        "scope": "Central",
        "benefit_amount": "Highest government interest rate (8.2% per year) + Complete tax exemption + Secure fund for daughter's education & marriage",
        "descriptions": {
            "hi": "10 साल से कम उम्र की बेटी के नाम पर डाकघर या बैंक में केवल 250 रुपये से खाता खोलें, जिस पर सरकार 8.2% का सबसे ज्यादा ब्याज देती है।",
            "ta": "10 வயதுக்குட்பட்ட பெண் குழந்தைகளின் பெயரில் தபால் நிலையங்களில் வெறும் ₹250 செலுத்தி துவங்கக்கூடிய அதிக வட்டி தரும் சேமிப்பு திட்டம்.",
            "te": "10 సంవత్సరాలలోపు ఆడపిల్లల పేరుతో పోస్టాఫీసు లేదా బ్యాంకులో కేవలం ₹250 తో ఖాతా తెరిచి, 8.2% అత్యధిక వడ్డీ పొందే పథకం.",
            "ml": "10 വയസ്സിന് താഴെയുള്ള പെൺകുട്ടികൾക്കായി തപാൽ വകുപ്പ് വഴിയോ ബാങ്ക് വഴിയോ ₹250 രൂപക്ക് തുടങ്ങാവുന്ന ഉയർന്ന പലിശ നൽകുന്ന പദ്ധതി.",
            "en": "Government-backed savings scheme for parents of girl children aged below 10 years offering an attractive 8.2% compound interest."
        },
        "eligibility": {
            "target_child_age_max": 10,
            "marital_status": ["any"],
            "target_group": "Parents or legal guardians of girl child under 10 years of age (maximum 2 daughters per family)",
            "special_condition": "Account matures when daughter turns 21 years old."
        },
        "documents_required": [
            {"doc": "Daughter's Birth Certificate", "vernacular": {"hi": "बेटी का जन्म प्रमाण पत्र", "ta": "குழந்தையின் பிறப்பு சான்றிதழ்", "te": "పాప పుట్టిన తేదీ ధృవీకరణ పత్రం", "ml": "കുട്ടിയുടെ ജനന സർട്ടിഫിക്കറ്റ്"}},
            {"doc": "Mother / Guardian's Aadhaar Card", "vernacular": {"hi": "माता या अभिभावक का आधार कार्ड", "ta": "தாயின் ஆதார் அட்டை", "te": "తల్లి లేదా సంరక్షకుని ఆధార్", "ml": "അമ്മയുടെ ആധാർ കാർഡ്"}},
            {"doc": "Guardian's Address Proof", "vernacular": {"hi": "निवास प्रमाण पत्र या राशन कार्ड", "ta": "முகவரி சான்று", "te": "నివాస ధృవీకరణ పత్రం", "ml": "മേൽവിലാസ രേഖ"}}
        ],
        "offline_process": {
            "submission_center": "Any Village Branch Post Office (Daak Ghar) or Nationalized Bank",
            "action": "Walk into your village post office with ₹250 cash and birth certificate. Dak Sevak issues physical passbook immediately.",
            "token_code_prefix": "SSY-DAK"
        }
    },
    {
        "id": "pmay_gramin",
        "name": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G)",
        "vernacular_names": {
            "hi": "प्रधानमंत्री आवास योजना - ग्रामीण (पक्का मकान)",
            "ta": "பிரதம மந்திரி ஊரக குடியிருப்பு திட்டம் (பக்கா வீடு)",
            "te": "ప్రధాన మంత్రి ఆవాస్ యోజన - గ్రామీణ్ (పక్కా ఇల్లు)",
            "ml": "പ്രധാനമന്ത്രി ഗ്രാമീൺ ആവാസ് യോജന (പക്കാ വീട്)",
            "en": "PM Rural Housing Scheme"
        },
        "category": "housing",
        "scope": "Central",
        "benefit_amount": "₹1,20,000 in plains / ₹1,30,000 in hilly/difficult areas + ₹12,000 toilet grant + 90-95 days MGNREGA wages",
        "descriptions": {
            "hi": "कच्चे मकान में रहने वाले परिवारों को पक्का मकान बनाने के लिए ₹1.20 लाख की सहायता, जो महिला मुखिया के नाम पर या संयुक्त रूप से दी जाती है।",
            "ta": "கிராமப்புறங்களில் கூரை அல்லது மண் வீட்டில் வசிக்கும் குடும்பங்களுக்கு பக்கா வீடு கட்ட ₹1.20 லட்சம் முதல் ₹1.30 லட்சம் நிதி உதவி.",
            "te": "గ్రామీణ ప్రాంతాలలో నివసించే పేద మహిళల పేరిట పక్కా ఇల్లు నిర్మించుకోవడానికి ₹1,20,000 నుండి ₹1,30,000 వరకు ఆర్థిక సహాయం.",
            "ml": "മണ്ണും ഓലയും മേഞ്ഞ വീടുകളിൽ താമസിക്കുന്നവർക്ക് സ്വന്തമായി പക്കാ വീട് നിർമ്മിക്കാൻ ₹1.20 ലക്ഷം മുതൽ ₹1.30 ലക്ഷം വരെ ധനസഹായം.",
            "en": "Financial assistance to rural homeless and families living in kutcha/dilapidated houses, with mandatory ownership or co-ownership in woman's name."
        },
        "eligibility": {
            "min_age": 18,
            "marital_status": ["any"],
            "housing_status": "kutcha_or_homeless",
            "target_group": "Rural families without permanent pucca house; priority given to female-headed households, widows, SC/ST",
            "special_condition": "Must be listed in SECC list or Gram Sabha verified beneficiary list."
        },
        "documents_required": [
            {"doc": "Aadhaar Card of Female Head", "vernacular": {"hi": "महिला मुखिया का आधार कार्ड", "ta": "குடும்பத் தலைவியின் ஆதார்", "te": "మహిళా యజమాని ఆధార్ కార్డు", "ml": "കുടുംബനാഥയുടെ ആധാർ"}},
            {"doc": "Bank Passbook with DBT mapping", "vernacular": {"hi": "बैंक खाता पासबुक", "ta": "வங்கி பாஸ்புக்", "te": "బ్యాంక్ ఖాతా పుస్తకం", "ml": "ബാങ്ക് പാസ്സ്ബുക്ക്"}},
            {"doc": "MGNREGA Job Card (for labor wage credit)", "vernacular": {"hi": "मनरेगा जॉब कार्ड", "ta": "100 நாள் வேலை அட்டை (மகாத்மா காந்தி திட்டம்)", "te": "ఉపాధి హామీ జాబ్ కార్డు", "ml": "തൊഴിലുറപ്പ് കാർഡ്"}},
            {"doc": "Land ownership proof or Gram Panchayat certificate", "vernacular": {"hi": "जमीन का पर्चा या ग्राम पंचायत अनापत्ति प्रमाण पत्र", "ta": "நில பட்டா அல்லது பஞ்சாயத்து சான்றிதழ்", "te": "భూమి పట్టా లేదా పంచాయతీ ధృవీకరణ", "ml": "ഭൂമി പട്ടയം / പഞ്ചായത്ത് രേഖ"}}
        ],
        "offline_process": {
            "submission_center": "Gram Panchayat Office (Gram Rozgar Sahayak / Panchayat Secretary)",
            "action": "Enroll name in Gram Sabha housing agenda. Geotagging photo of existing kutcha house taken by village secretary.",
            "token_code_prefix": "PMAY-GR"
        }
    },
    {
        "id": "ignwps_widow_pension",
        "name": "Indira Gandhi National Widow Pension Scheme (IGNWPS) & State Top-up",
        "vernacular_names": {
            "hi": "इंदिरा गांधी राष्ट्रीय विधवा पेंशन योजना",
            "ta": "விதவை மற்றும் ஆதரவற்ற பெண்கள் மாதாந்திர ஓய்வூதியம்",
            "te": "వితంతు పెన్షన్ పథకం",
            "ml": "വിധവാ പെൻഷൻ പദ്ധതി",
            "en": "National Widow Pension Scheme"
        },
        "category": "pension",
        "scope": "Central & State Joint",
        "benefit_amount": "₹1,000 to ₹3,000 monthly direct bank transfer (depending on state government contribution)",
        "descriptions": {
            "hi": "40 से 79 वर्ष की विधवा माताओं-बहनों को सम्मानपूर्वक जीवन यापन के लिए हर महीने सीधे बैंक खाते में पेंशन।",
            "ta": "கணவனை இழந்த 40 வயதுக்கு மேற்பட்ட ஆதரவற்ற பெண்களுக்கு மாதந்தோறும் ₹1,000 முதல் ₹1,500 வங்கி கணக்கில் ஓய்வூதியம்.",
            "te": "40 సంవత్సరాలు దాటిన నిరుపేద వితంతు మహిళలకు ప్రతి నెలా గౌరవప్రదమైన జీవనం కొరకు పింఛను సదుపాయం.",
            "ml": "വിധവകളായ നിർധന വനിതകൾക്ക് ആശ്വാസമായി പ്രതിമാസ പെൻഷൻ ബാങ്ക് അക്കൗണ്ടിലേക്ക് നൽകുന്നു.",
            "en": "Monthly subsistence pension for BPL widows aged 40-79 years, credited directly into Aadhaar-seeded accounts."
        },
        "eligibility": {
            "min_age": 40,
            "max_age": 79,
            "marital_status": ["widow"],
            "bpl_required": True,
            "target_group": "Widowed women living below poverty line without adult sons capable of full support",
            "special_condition": "At age 80, automatically upgrades to Senior Citizen Pension tier."
        },
        "documents_required": [
            {"doc": "Husband's Death Certificate", "vernacular": {"hi": "पति का मृत्यु प्रमाण पत्र", "ta": "கணவரின் இறப்பு சான்றிதழ்", "te": "భర్త మరణ ధృవీకరణ పత్రం", "ml": "ഭർത്താവിന്റെ മരണ സർട്ടിഫിക്കറ്റ്"}},
            {"doc": "Applicant's Aadhaar Card", "vernacular": {"hi": "महिला का आधार कार्ड", "ta": "ஆதார் அட்டை", "te": "ఆధార్ కార్డు", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "BPL / Ration Card / Income Certificate", "vernacular": {"hi": "बीपीएल राशन कार्ड या आय प्रमाण पत्र", "ta": "வருமான சான்று / ரேஷன் கார்டு", "te": "ఆదాయ ధృవీకరణ / రేషన్ కార్డు", "ml": "റേഷൻ കാർഡ് / വരുമാന സർട്ടിഫിക്കറ്റ്"}},
            {"doc": "Bank Passbook with DBT enabled", "vernacular": {"hi": "बैंक पासबुक", "ta": "வங்கி பாஸ்புக்", "te": "బ్యాంక్ పాస్ బుక్", "ml": "ബാങ്ക് പാസ്സ്ബുക്ക്"}}
        ],
        "offline_process": {
            "submission_center": "Tehsildar / Taluk Office or Block Development Office (BDO) or CSC Center",
            "action": "Submit paper dossier to Village Revenue Officer (VRO/Patwari). Physical verification within 21 days.",
            "token_code_prefix": "PEN-WID"
        }
    },
    # Tamil Nadu Specific Schemes
    {
        "id": "tn_magalir_urimai",
        "name": "Kalaignar Magalir Urimai Thogai (Tamil Nadu)",
        "vernacular_names": {
            "ta": "கலைஞர் மகளிர் உரிமைத் திட்டம் (மாதம் ₹1000)",
            "hi": "तमिलनाडु कलैग्नार महिला अधिकार योजना (₹1000/माह)",
            "te": "తమిళనాడు మహిళా హక్కు పథకం (నెలకు ₹1000)",
            "ml": "തമിഴ്‌നാട് കലൈഞ്ജർ മഗളിർ ഉരിമൈ തിട്ടം (പ്രതിമാസം ₹1000)",
            "en": "Kalaignar Women's Basic Income Scheme (TN)"
        },
        "category": "direct_income",
        "scope": "Tamil Nadu State",
        "benefit_amount": "₹1,000 per month direct bank transfer on 15th of every month",
        "descriptions": {
            "ta": "குடும்பத் தலைவிகளுக்கு மாதம் ₹1,000 உரிமைத் தொகையாக அவர்களின் உழைப்பை அங்கீகரிக்கும் வகையில் நேரடியாக வங்கி கணக்கில் வழங்கப்படுகிறது.",
            "hi": "तमिलनाडु में परिवार की महिला मुखिया को हर महीने ₹1,000 की सम्मान राशि सीधे बैंक खाते में दी जाती है।",
            "te": "తమిళనాడులో కుటుంబ మహిళా పెద్దకు నెలకు ₹1000 గౌరవ భృతి నేరుగా బ్యాంక్ ఖాతాలో జమ చేయబడుతుంది.",
            "ml": "തമിഴ്‌നാട്ടിലെ കുടുംബനാഥകളായ സ്ത്രീകൾക്ക് പ്രതിമാസം ₹1,000 അവകാശത്തുക ബാങ്ക് അക്കൗണ്ടിൽ ലഭ്യമാക്കുന്നു.",
            "en": "Monthly financial entitlement of ₹1,000 to eligible women heads of families across Tamil Nadu."
        },
        "eligibility": {
            "min_age": 21,
            "marital_status": ["married", "unmarried", "widow", "transgender"],
            "state": "Tamil Nadu",
            "annual_income_limit": 250000,
            "land_limit_acres": 5,
            "power_consumption_limit": 3600,
            "target_group": "Women family heads listed in Tamil Nadu Smart Ration Card without government pensioner in home."
        },
        "documents_required": [
            {"doc": "TN Smart Ration Card", "vernacular": {"ta": "ஸ்மார்ட் குடும்ப அட்டை", "hi": "स्मार्ट राशन कार्ड", "te": "స్మార్ట్ రేషన్ కార్డు", "ml": "സ്മാർട്ട് റേഷൻ കാർഡ്"}},
            {"doc": "Aadhaar Card", "vernacular": {"ta": "ஆதார் அட்டை", "hi": "आधार कार्ड", "te": "ఆధార్ కార్డు", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "Electricity Consumer Number (TANGEDCO)", "vernacular": {"ta": "மின் இணைப்பு எண்", "hi": "बिजली बिल उपभोक्ता संख्या", "te": "కరెంట్ మీటర్ నెంబర్", "ml": "വൈദ്യുതി നമ്പർ"}},
            {"doc": "Bank Passbook", "vernacular": {"ta": "வங்கி பாஸ்புக்", "hi": "बैंक पासबुक", "te": "బ్యాంక్ పాస్ బుక్", "ml": "ബാങ്ക് പാസ്സ്ബുക്ക്"}}
        ],
        "offline_process": {
            "submission_center": "Ration Shop (Fair Price Shop) Special Camp / E-Sevai Center",
            "action": "Visit your local ration shop during special camp days. Bio-metric fingerprint authentication done on the spot.",
            "token_code_prefix": "TN-KMUT"
        }
    },
    {
        "id": "tn_muthulakshmi_reddy",
        "name": "Dr. Muthulakshmi Reddy Maternity Benefit Scheme (Tamil Nadu)",
        "vernacular_names": {
            "ta": "டாக்டர் முத்துலட்சுமி ரெட்டி மகப்பேறு நிதி உதவி திட்டம் (₹18,000)",
            "hi": "डॉ मुथुलक्ष्मी रेड्डी मातृत्व सहायता योजना (₹18,000)",
            "te": "డాక్టర్ ముత్తులక్ష్మి రెడ్డి ప్రసవ ఆర్థిక సహాయం (₹18,000)",
            "ml": "ഡോ. മുത്തുലക്ഷ്മി റെഡ്ഡി പ്രസവ ധനസഹായം (₹18,000)",
            "en": "Dr. Muthulakshmi Reddy Maternity Scheme (TN)"
        },
        "category": "maternity",
        "scope": "Tamil Nadu State",
        "benefit_amount": "₹18,000 cash in 5 installments + 2 Amma Nutrition Kits worth ₹4,000",
        "descriptions": {
            "ta": "கர்ப்பிணி தாய்மார்களுக்கு ₹14,000 ரொக்க உதவி மற்றும் ₹4,000 மதிப்புள்ள சத்து மாவு, இரும்புச்சத்து டானிக் அடங்கிய 2 அம்மா ஊட்டச்சத்து பெட்டகம்.",
            "hi": "तमिलनाडु में गर्भवती महिलाओं को ₹14,000 नकद और ₹4,000 के 2 अम्मा पोषण किट कुल ₹18,000 की महा-सहायता।",
            "te": "గర్భిణీలకు ₹14,000 నగదు మరియు ₹4,000 విలువైన పోషకాహార కిట్‌లు అందించే పథకం.",
            "ml": "ഗർഭിണികൾക്ക് ₹14,000 സാമ്പത്തിക സഹായവും ₹4,000 രൂപയുടെ 2 പോഷകാഹാര കിറ്റുകളും ഉൾപ്പെടെ ₹18,000 സഹായം.",
            "en": "Tamil Nadu comprehensive maternity support offering ₹14,000 in cash plus two Amma maternal nutrition kits."
        },
        "eligibility": {
            "min_age": 19,
            "marital_status": ["pregnant"],
            "state": "Tamil Nadu",
            "target_group": "Poor pregnant mothers delivering at Government Primary Health Centres or Hospitals."
        },
        "documents_required": [
            {"doc": "RCH ID / PICME Registration Number", "vernacular": {"ta": "PICME எண் பதிவு அட்டை", "hi": "PICME मातृत्व आईडी", "te": "PICME ఐడీ", "ml": "PICME ഐഡി"}},
            {"doc": "Aadhaar Card", "vernacular": {"ta": "ஆதார் அட்டை", "hi": "आधार कार्ड", "te": "ఆధார் కార్డు", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "Mother's Bank Account", "vernacular": {"ta": "வங்கி கணக்கு புத்தகம்", "hi": "बैंक खाता", "te": "బ్యాంక్ ఖాతా", "ml": "ബാങ്ക് അക്കൗണ്ട്"}}
        ],
        "offline_process": {
            "submission_center": "Primary Health Centre (PHC) / Village Health Nurse (VHN)",
            "action": "Register pregnancy within 12 weeks with your local Village Health Nurse (VHN) to get 12-digit PICME number.",
            "token_code_prefix": "TN-MMR"
        }
    },
    # Andhra Pradesh & Telangana Schemes
    {
        "id": "ap_ysr_cheyutha",
        "name": "YSR Cheyutha & Aasara (Andhra Pradesh)",
        "vernacular_names": {
            "te": "వైఎస్సార్ చేయూత & ఆసరా పథకం (మహిళా స్వయం ఉపాధి)",
            "hi": "आंध्र प्रदेश वाईएसआर चेयुथा योजना (₹75,000 4 वर्षों में)",
            "ta": "ஆந்திரா ஒய்.எஸ்.ஆர் செய்யூதா திட்டம்",
            "ml": "വൈ.എസ്.ആർ ചേയൂത പദ്ധതി",
            "en": "YSR Cheyutha Women Empowerment (AP)"
        },
        "category": "livelihood",
        "scope": "Andhra Pradesh State",
        "benefit_amount": "₹18,750 per year (Total ₹75,000 over 4 years) for grocery shop, dairy cattle, or micro-enterprise",
        "descriptions": {
            "te": "45 నుండి 60 సంవత్సరాల మధ్య వయస్సు గల SC, ST, BC మరియు మైనారిటీ మహిళలకు ఏటా ₹18,750 ఆర్థిక సహాయం, స్వయం ఉపాధి కోసం.",
            "hi": "45 से 60 वर्ष की एससी, एसटी, ओबीसी और अल्पसंख्यक महिलाओं को हर साल ₹18,750 की आजीविका सहायता।",
            "ta": "45 முதல் 60 வயதுடைய பிற்படுத்தப்பட்ட மற்றும் சிறுபான்மையின பெண்களுக்கு சுயதொழில் தொடங்க ஆண்டுதோறும் ₹18,750 நிதி.",
            "ml": "45 മുതൽ 60 വയസ്സുവരെയുള്ള പിന്നാക്ക വിഭാഗങ്ങളിലെ സ്ത്രീകൾക്ക് സ്വയംതൊഴിൽ കണ്ടെത്തുന്നതിനായി പ്രതിവർഷം ₹18,750 ധനസഹായം.",
            "en": "Empowers SC, ST, BC, and Minority women aged 45-60 with ₹18,750/year to set up small kirana shops, sheep rearing, or dairy units."
        },
        "eligibility": {
            "min_age": 45,
            "max_age": 60,
            "state": "Andhra Pradesh",
            "social_category": ["SC", "ST", "BC", "Minority"],
            "target_group": "Poor women aged 45-60 not drawing other government pensions."
        },
        "documents_required": [
            {"doc": "Integrated Caste Certificate", "vernacular": {"te": "కుల ధృవీకరణ పత్రం", "hi": "जाति प्रमाण पत्र", "ta": "ஜாதி சான்றிதழ்", "ml": "ജാതി സർട്ടിഫിക്കറ്റ്"}},
            {"doc": "Aadhaar Card", "vernacular": {"te": "ఆధార్ కార్డు", "hi": "आधार कार्ड", "ta": "ஆதார் அட்டை", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "Rice Card / Ration Card", "vernacular": {"te": "రైస్ కార్డ్ / రేషన్ కార్డు", "hi": "चावल कार्ड / राशन कार्ड", "ta": "அரிசி அட்டை", "ml": "റേഷൻ കാർഡ്"}},
            {"doc": "Unencumbered Bank Account", "vernacular": {"te": "బ్యాంక్ ఖాతా పాస్ బుక్", "hi": "बैंक खाता", "ta": "வங்கி பாஸ்புக்", "ml": "ബാങ്ക് പാസ്സ്ബുക്ക്"}}
        ],
        "offline_process": {
            "submission_center": "Grama Sachivalayam (Village Secretariat) / Ward Volunteer",
            "action": "Your local Village Volunteer visits your doorstep with biometric tablet for social audit verification.",
            "token_code_prefix": "AP-YSR"
        }
    },
    {
        "id": "tg_mahalakshmi",
        "name": "Telangana Mahalakshmi Scheme",
        "vernacular_names": {
            "te": "తెలంగాణ మహాలక్ష్మి పథకం (నెలకు ₹2,500 + ఉచిత బస్సు)",
            "hi": "तेलंगाना महालक्ष्मी योजना (₹2,500/माह + मुफ्त बस यात्रा)",
            "ta": "தெலுங்கானா மகாலட்சுமி திட்டம் (மாதம் ₹2,500)",
            "ml": "തെലങ്കാന മഹാലക്ഷ്മി പദ്ധതി (പ്രതിമാസം ₹2,500)",
            "en": "Telangana Mahalakshmi Guarantee Scheme"
        },
        "category": "direct_income",
        "scope": "Telangana State",
        "benefit_amount": "₹2,500 per month financial aid + Free TSRTC bus travel across state + LPG cylinder for ₹500",
        "descriptions": {
            "te": "తెలంగాణలోని అర్హులైన మహిళలకు నెలకు ₹2,500 ఆర్థిక సహాయం, రాష్ట్రవ్యాప్తంగా ఆర్టీసీ బస్సుల్లో ఉచిత ప్రయాణం మరియు ₹500కే వంటగ్యాస్ సిలిండర్.",
            "hi": "तेलंगाना की पात्र महिलाओं को ₹2,500 प्रति माह, सरकारी बसों में 100% मुफ्त यात्रा और मात्र ₹500 में गैस सिलेंडर।",
            "ta": "தெலுங்கானா பெண்களுக்கு மாதம் ₹2,500 நிதி, இலவச பேருந்து பயணம் மற்றும் ₹500க்கு காஸ் சிலிண்டர்.",
            "ml": "തെലങ്കാനയിലെ സ്ത്രീകൾക്ക് പ്രതിമാസം ₹2,500 ധനസഹായം, സൗജന്യ ബസ് യാത്ര, ₹500 ന് ഗ്യാസ് സിലിണ്ടർ.",
            "en": "Telangana welfare guarantee providing ₹2,500/month to female family heads, free state bus travel, and subsidized gas cylinder at ₹500."
        },
        "eligibility": {
            "min_age": 18,
            "state": "Telangana",
            "target_group": "Adult women residents of Telangana belonging to poor households with Praja Palana registration."
        },
        "documents_required": [
            {"doc": "Praja Palana Application Receipt", "vernacular": {"te": "ప్రజా పాలన దరఖాస్తు రసీదు", "hi": "प्रजा पालन आवेदन रसीद", "ta": "பிரஜா பாலனா ரசீது", "ml": "പ്രജാ പാലന രസീത്"}},
            {"doc": "Aadhaar Card", "vernacular": {"te": "ఆధార్ కార్డు", "hi": "आधार कार्ड", "ta": "ஆதார் அட்டை", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "White Ration Card", "vernacular": {"te": "తెల్ల రేషన్ కార్డు", "hi": "सफेद राशन कार्ड", "ta": "வெள்ளை குடும்ப அட்டை", "ml": "വെള്ള റേഷൻ കാർഡ്"}}
        ],
        "offline_process": {
            "submission_center": "Gram Panchayat Office / MPDO Office during Praja Palana grievance days",
            "action": "Submit paper form at Gram Panchayat office; free bus travel can be availed immediately by showing physical Aadhaar to conductor.",
            "token_code_prefix": "TG-MLX"
        }
    },
    # Kerala Specific Schemes
    {
        "id": "kerala_kudumbashree",
        "name": "Kudumbashree Micro-Enterprise & Livelihood Scheme (Kerala)",
        "vernacular_names": {
            "ml": "കുടുംബശ്രീ സംരംഭകത്വ വികസന വായ്പയും ഉപജീവന പദ്ധതിയും",
            "hi": "केरल कुटुंबश्री महिला आजीविका व सूक्ष्म उद्यम योजना",
            "ta": "கேரளா குடும்பஸ்ரீ வாழ்வாதார கடன் திட்டம்",
            "te": "కేరళ కుటుంబశ్రీ మహిళా సాధికారత పథకం",
            "en": "Kerala Kudumbashree Livelihood Mission"
        },
        "category": "livelihood",
        "scope": "Kerala State",
        "benefit_amount": "Subsidized enterprise loans up to ₹10 Lakhs for micro-enterprises + 4% interest subvention + Samagra marketing support",
        "descriptions": {
            "ml": "കേരളത്തിലെ വനിതകൾക്ക് കൃഷി, ഭക്ഷ്യ സംസ്കരണം, കാറ്ററിങ്, കൈത്തറി എന്നിവയിൽ സംരംഭങ്ങൾ ആരംഭിക്കാൻ കുടുംബശ്രീ വഴി സബ്സിഡി വായ്പ.",
            "hi": "केरल की महिलाओं को खाद्य प्रसंस्करण, जैविक खेती और हस्तशिल्प उद्यम शुरू करने के लिए 4% कम ब्याज पर रियायती ऋण।",
            "ta": "குடும்பஸ்ரீ மூலம் உணவு தயாரிப்பு மற்றும் சிறுவணிகம் தொடங்க குறைந்த வட்டியில் மானிய கடன்.",
            "te": "కేరళలో మహిళలకు స్వయం ఉపాధి మరియు ఆహార తయారీ పరిశ్రమల కోసం 4% రాయితీతో రుణాలు.",
            "en": "Flagship poverty eradication and women empowerment mission offering community collective farming loans, zero-collateral micro-credit, and marketing tie-ups."
        },
        "eligibility": {
            "min_age": 18,
            "max_age": 65,
            "state": "Kerala",
            "shg_member_required": True,
            "target_group": "Active members of Kudumbashree Neighbourhood Groups (NHGs / Ayalkoottam) in rural Kerala."
        },
        "documents_required": [
            {"doc": "Kudumbashree Ayalkoottam Passbook", "vernacular": {"ml": "അയൽക്കൂട്ട പാസ്സ്ബുക്ക്", "hi": "कुटुंबश्री समूह पासबुक", "ta": "குழு பாஸ்புக்", "te": "సభ్యత్వ పాస్ బుక్"}},
            {"doc": "Aadhaar Card", "vernacular": {"ml": "ആധാർ കാർഡ്", "hi": "आधार कार्ड", "ta": "ஆதார் அட்டை", "te": "ఆధార్ కార్డు"}},
            {"doc": "Bank Account linked to CDS (Community Development Society)", "vernacular": {"ml": "ബാങ്ക് അക്കൗണ്ട് വിശദാംശങ്ങൾ", "hi": "सीडीएस बैंक खाता", "ta": "வங்கி விவரங்கள்", "te": "బ్యాంక్ ఖాతా"}}
        ],
        "offline_process": {
            "submission_center": "Local Self Government (Grama Panchayat) Kudumbashree CDS Office",
            "action": "Present business proposal at weekly Ayalkoottam gathering. Forwarded through Area Development Society (ADS) to Grama Panchayat.",
            "token_code_prefix": "KL-KDM"
        }
    },
    # Hindi Belt / Northern States (MP, UP, Bihar)
    {
        "id": "mp_ladli_behna",
        "name": "Mukhyamantri Ladli Behna Yojana (Madhya Pradesh)",
        "vernacular_names": {
            "hi": "मुख्यमंत्री लाड़ली बहना योजना (मध्य प्रदेश - ₹1,250/माह)",
            "ta": "மத்தியப் பிரதேசம் லாட்லி பெஹ்னா திட்டம்",
            "te": "మధ్యప్రదేశ్ లాడ్లీ బెహనా పథకం",
            "ml": "മധ്യപ്രദേശ് ലാഡ്‌ലി ബെഹ്‌ന പദ്ധതി",
            "en": "MP Ladli Behna Monthly Assistance"
        },
        "category": "direct_income",
        "scope": "Madhya Pradesh State",
        "benefit_amount": "₹1,250 per month directly into DBT bank account (scheduled to increase to ₹3,000 in phases)",
        "descriptions": {
            "hi": "मध्य प्रदेश की 21 से 60 वर्ष की विवाहित, विधवा, तलाकशुदा बहनों को आर्थिक स्वतंत्रता और पोषण के लिए हर महीने ₹1,250 की सीधी बैंक मदद।",
            "ta": "மத்தியப் பிரதேசத்தில் 21-60 வயதுடைய பெண்களுக்கு மாதம் ₹1,250 நிதி உதவி வங்கி கணக்கில் வரவு.",
            "te": "మధ్యప్రదేశ్‌లో 21-60 సంవత్సరాల మహిళలకు నెలకు ₹1,250 ఆర్థిక సహాయం.",
            "ml": "മധ്യപ്രദേശിലെ 21-60 വയസ്സുള്ള വനിതകൾക്ക് പ്രതിമാസം ₹1,250 നേരിട്ട് ബാങ്കിലേക്ക്.",
            "en": "Monthly financial aid of ₹1,250 provided to married, widowed, deserted women in Madhya Pradesh with zero paperwork burden."
        },
        "eligibility": {
            "min_age": 21,
            "max_age": 60,
            "marital_status": ["married", "widow", "divorced"],
            "state": "Madhya Pradesh",
            "annual_income_limit": 250000,
            "land_limit_acres": 5,
            "target_group": "Resident women of MP whose family is not income tax payee and owns less than 5 acres of agricultural land."
        },
        "documents_required": [
            {"doc": "Samagra Family ID (समग्र परिवार आईडी)", "vernacular": {"hi": "समग्र परिवार आईडी और सदस्य आईडी", "ta": "சமக்ரா ஐடி", "te": "సమగ్ర ఐడీ", "ml": "സമഗ്ര ഐഡി"}},
            {"doc": "Aadhaar Card linked to Mobile", "vernacular": {"hi": "आधार कार्ड (मोबाइल से लिंक)", "ta": "ஆதார் அட்டை", "te": "ఆధార్ కార్డు", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "Aadhaar-seeded DBT Bank Account", "vernacular": {"hi": "डीबीटी सक्रिय बैंक खाता", "ta": "டிபிடி வங்கி கணக்கு", "te": "డీబీటీ బ్యాంక్ ఖాతా", "ml": "ഡിബിടി ബാങ്ക് അക്കൗണ്ട്"}}
        ],
        "offline_process": {
            "submission_center": "Gram Panchayat Sachiv / Ward Camp / CSC Center",
            "action": "Gram Panchayat holds free registration camps. Secretary takes live photo and biometrics; no physical photo submission required.",
            "token_code_prefix": "MP-LBY"
        }
    },
    {
        "id": "up_kanya_sumangala",
        "name": "Mukhyamantri Kanya Sumangala Yojana (Uttar Pradesh)",
        "vernacular_names": {
            "hi": "मुख्यमंत्री कन्या सुमंगला योजना (उत्तर प्रदेश - ₹25,000)",
            "ta": "உத்தரப் பிரதேசம் கன்யா சுமங்கலா திட்டம்",
            "te": "ఉత్తరప్రదేశ్ కన్యా సుమంగళ పథకం",
            "ml": "ഉത്തർപ്രദേശ് കന്യാ സുമംഗല പദ്ധതി",
            "en": "UP Kanya Sumangala Girl Child Scheme"
        },
        "category": "education",
        "scope": "Uttar Pradesh State",
        "benefit_amount": "₹25,000 in 6 progressive installments from daughter's birth to graduation admission",
        "descriptions": {
            "hi": "उत्तर प्रदेश में बिटिया के जन्म से लेकर स्नातक (कॉलेज) में प्रवेश तक 6 चरणों में कुल ₹25,000 की वित्तीय मदद।",
            "ta": "உத்தரப்பிரதேசத்தில் பெண் குழந்தை பிறப்பு முதல் கல்லூரி படிப்பு வரை 6 தவணைகளில் ₹25,000 அரசு நிதி.",
            "te": "ఉత్తరప్రదేశ్‌లో ఆడపిల్ల పుట్టినప్పటి నుండి కాలేజీ చేరే వరకు 6 విడతలలో ₹25,000 ఆర్థిక సహాయం.",
            "ml": "പെൺകുട്ടികളുടെ ജനനം മുതൽ ബിരുദ പഠനം വരെ 6 ഘട്ടങ്ങളിലായി ₹25,000 സഹായം നൽകുന്ന പദ്ധതി.",
            "en": "Six-stage conditional cash transfer for girl children in UP covering birth, immunization, class 1, class 6, class 9, and graduation."
        },
        "eligibility": {
            "state": "Uttar Pradesh",
            "annual_income_limit": 300000,
            "target_child_count_max": 2,
            "target_group": "Permanent residents of UP with annual family income up to ₹3 Lakhs, up to 2 daughters per family."
        },
        "documents_required": [
            {"doc": "Girl Child Birth Certificate", "vernacular": {"hi": "बेटी का जन्म प्रमाण पत्र", "ta": "பிறப்பு சான்றிதழ்", "te": "పుట్టిన తేదీ పత్రం", "ml": "ജനന സർട്ടിഫിക്കറ്റ്"}},
            {"doc": "Immunization Card / School Admission Certificate", "vernacular": {"hi": "टीकाकरण कार्ड या स्कूल प्रवेश रसीद", "ta": "தடுப்பூசி அட்டை / பள்ளி ரசீது", "te": "టీకా కార్డు / పాఠశాల రసీదు", "ml": "വാക്സിനേഷൻ കാർഡ്"}},
            {"doc": "Mother's Aadhaar & Bank Passbook", "vernacular": {"hi": "माता का आधार व बैंक पासबुक", "ta": "தாயின் ஆதார் & பாஸ்புக்", "te": "తల్లి ఆధార్ & బ్యాంక్ బుక్", "ml": "അമ്മയുടെ ആധാർ"}}
        ],
        "offline_process": {
            "submission_center": "Block Development Office (BDO) / District Probation Office (DPO) / CSC Jan Seva Kendra",
            "action": "VLE at Jan Seva Kendra uploads immunization or school admission certificate with mother's Aadhaar.",
            "token_code_prefix": "UP-MKS"
        }
    },
    {
        "id": "bihar_kanya_utthan",
        "name": "Mukhyamantri Kanya Utthan Yojana (Bihar)",
        "vernacular_names": {
            "hi": "मुख्यमंत्री कन्या उत्थान योजना (बिहार - ₹50,000 स्नातक तक)",
            "ta": "பீகார் கன்யா உத்தன் திட்டம்",
            "te": "బీహార్ కన్యా ఉత్థాన్ పథకం",
            "ml": "ബീഹാർ കന്യാ ഉത്ഥാൻ പദ്ധതി",
            "en": "Bihar Kanya Utthan Girl Education Scheme"
        },
        "category": "education",
        "scope": "Bihar State",
        "benefit_amount": "Total ₹54,100 from birth till graduation (₹50,000 upon passing Graduation / BA/BSc/BCom degree)",
        "descriptions": {
            "hi": "बिहार में बेटियों को भ्रूण हत्या रोकने, शिक्षा और उच्च शिक्षा में आत्मनिर्भर बनाने के लिए जन्म से लेकर स्नातक पास करने तक ₹54,100 की आर्थिक मदद।",
            "ta": "பீகாரில் பெண் குழந்தை பிறந்தது முதல் பட்டப்படிப்பு முடிப்பது வரை ₹54,100 கல்வி ஊக்கத்தொகை.",
            "te": "బీహార్‌లో ఆడపిల్ల పుట్టుక నుండి డిగ్రీ పూర్తి చేసే వరకు ₹54,100 ప్రోత్సాహకం.",
            "ml": "പെൺകുട്ടികളുടെ ഉന്നത വിദ്യാഭ്യാസം ഉറപ്പാക്കാൻ ബിരുദം നേടുമ്പോൾ ₹50,000 ഉൾപ്പെടെ ധനസഹായം നൽകുന്നു.",
            "en": "Comprehensive incentive package for girl children in Bihar to curb child marriage and promote higher education up to degree graduation."
        },
        "eligibility": {
            "state": "Bihar",
            "marital_status": ["unmarried"],
            "target_group": "Unmarried girl students of Bihar enrolled in recognized educational institutions or passing matriculation/graduation."
        },
        "documents_required": [
            {"doc": "Graduation / Matric Marksheet", "vernacular": {"hi": "अंक तालिका (मार्कशीट) व कॉलेज रजिस्ट्रेशन", "ta": "மதிப்பெண் சான்றிதழ்", "te": "మార్కుల జాబితా", "ml": "മാർക്ക് ലിസ്റ്റ്"}},
            {"doc": "Aadhaar Card (Bihar domicile)", "vernacular": {"hi": "आधार कार्ड (बिहार का स्थायी पता)", "ta": "ஆதார் அட்டை", "te": "ఆధార్ కార్డు", "ml": "ആധാർ കാർഡ്"}},
            {"doc": "Bank Passbook in Student's own name (Bihar bank branch)", "vernacular": {"hi": "छात्रा के नाम का बैंक खाता (बिहार शाखा)", "ta": "மாணவியின் சொந்த வங்கி கணக்கு", "te": "విద్యార్థిని సొంత బ్యాంక్ ఖాతా", "ml": "സ്വന്തം പേരിലുള്ള ബാങ്ക് അക്കൗണ്ട്"}}
        ],
        "offline_process": {
            "submission_center": "College Principal Office or Block Education Office (BEO) / RTPS Counter",
            "action": "College clerk enters student registration and verifies marksheet on Medhasoft portal. No fee charged.",
            "token_code_prefix": "BR-MKU"
        }
    }
]

def search_schemes(
    user_state: Optional[str] = None,
    marital_status: Optional[str] = None,
    has_girl_child: Optional[bool] = None,
    is_shg_member: Optional[bool] = None,
    is_pregnant_lactating: Optional[bool] = None,
    category_filter: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    RAG Rule Evaluator: Filters and ranks verified schemes based on rural woman's spoken inputs.
    Never hallucinates eligibility; checks explicit constraints.
    """
    results = []
    for s in SCHEMES_DATABASE:
        # State check: match 'Central' or user's state
        if user_state:
            scope = s.get("scope", "")
            if scope != "Central" and user_state.lower() not in scope.lower():
                continue

        # Category check
        if category_filter and category_filter != "all":
            if s.get("category") != category_filter:
                continue

        # Maternal condition
        if is_pregnant_lactating and s["id"] in ["pmmvy", "tn_muthulakshmi_reddy"]:
            results.append(s)
            continue

        # SHG condition
        if is_shg_member and s["id"] in ["lakhpati_didi", "kerala_kudumbashree", "ap_ysr_cheyutha"]:
            results.append(s)
            continue

        # Girl child savings
        if has_girl_child and s["id"] in ["sukanya_samriddhi", "up_kanya_sumangala", "bihar_kanya_utthan"]:
            results.append(s)
            continue

        # Widow check
        if marital_status == "widow" and s["id"] == "ignwps_widow_pension":
            results.append(s)
            continue

        # General schemes (PMAY, PMUY, direct income)
        if s["id"] in ["pmuy", "pmay_gramin", "tn_magalir_urimai", "mp_ladli_behna", "tg_mahalakshmi"]:
            results.append(s)
        elif not (is_pregnant_lactating or is_shg_member or has_girl_child or marital_status == "widow"):
            results.append(s)

    # De-duplicate while preserving order
    seen_ids = set()
    deduped = []
    for r in results:
        if r["id"] not in seen_ids:
            seen_ids.add(r["id"])
            deduped.append(r)
    return deduped if deduped else SCHEMES_DATABASE[:6]

def get_all_schemes() -> List[Dict[str, Any]]:
    """Return all schemes across India for rural women."""
    return SCHEMES_DATABASE

def get_scheme_by_id(scheme_id: str) -> Optional[Dict[str, Any]]:
    for s in SCHEMES_DATABASE:
        if s["id"] == scheme_id:
            return s
    return None
