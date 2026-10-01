# 🇮🇳 VoiceSetu AI (वॉइस सेतु / குரல் சேது / వాయిస్ సేతు / വോയ്സ് സേതു)

### Audio-First Welfare Access for Rural Indian Women with Zero Prior Digital Knowledge

> **Core Philosophy**: Zero apps needed, zero typing needed, zero reading needed. Starts with a standard toll-free phone call (IVR) or WhatsApp voice notes in local dialects (Bhojpuri, Bundeli, Santhali, Kongu Tamil, Telangana Rural, Malabar Malayalam), grounded in verified official rules (RAG), backed by one-touch human fallback to Self-Help Group (SHG) Bank Sakhis, with built-in domestic safety camouflage.

---

## 🌟 Key Architecture & Constraint Solutions

### 1. No-App-First Paradigm
- **Toll-Free Phone Call (IVR Simulator)**: Uses standard feature phones or smartphones without installing any application. Operates via dial-in phone calls.
- **WhatsApp Voice Notes Mode**: For rural women with basic WhatsApp access who only communicate via the green microphone button. Accepts audio voice notes and responds with instant native spoken audio notes.

### 2. Audio-Only User Interface (No Reading Required)
- Every interaction is spoken aloud:
  - **Spoken Verbal Consent**: Explains privacy and asks for consent before proceeding.
  - **Spoken Keypad Confirmation**: Simple DTMF choices:
    - Press **1** or speak *"Haan / Aam / Avunu / Und"* for Yes.
    - Press **2** or speak *"Nahin / Illai / Kaadhu / Illa"* for No.
    - Press **9** to repeat audio prompt.
    - Press **\*** for instant domestic privacy camouflage.
  - **Spoken Document Checklist**: Audio guide on required physical documents (Aadhaar, Bank Passbook, Ration Card).
  - **Spoken Token & Appointment**: Issues spoken queue token and Gram Panchayat center details.

### 3. Local-Dialect ASR & Noisy Village Environment Testing
- Supported core languages:
  - **हिन्दी (Hindi)**: Standard, Bhojpuri, Bundeli accents.
  - **தமிழ் (Tamil)**: Standard, Kongu/Madurai regional vernacular.
  - **తెలుగు (Telugu)**: Standard, Telangana Rural, Rayalaseema dialects.
  - **മലയാളം (Malayalam)**: Standard, Malabar dialect.
- **Ambient Noise Simulator**:
  - Live sound level testing: **Quiet (30 dB)**, **Haat Bazaar (68 dB)**, **Tractor/Pump (78 dB)**, **Field Wind (62 dB)**.
  - Computes ASR confidence score in real time.
  - When background noise drops confidence below 65%, the agent immediately triggers human fallback.

### 4. Human Intermediary Fallback (Zero Abandonment)
- **One-Touch Escalation**:
  - Keypad button `DIDI` / `👩‍💼 SHG Didi`
  - Direct screen button: *"Connect SHG Bank Sakhi / CSC Didi Now"*
  - Voice trigger: User saying *"Didi"*, *"Help"*, or *"Samajh nahi aaya"*.
- **Gram Panchayat Worker Console**:
  - Escalates call to local village **Bank Sakhi (Sunita Devi)** or **CSC VLE operator**.
  - Worker sees caller phone, village, missing documents, and schedules doorstep biometric verification.

### 5. Retrieval-Augmented Generation (RAG) Over Official Schemes
Never hallucinates eligibility. Evaluates explicit rules across **14+ Central and State welfare schemes**:
- **Central Schemes**:
  1. *Pradhan Mantri Matru Vandana Yojana (PMMVY)*: ₹5,000 for 1st child, ₹6,000 for 2nd girl child.
  2. *Lakhpati Didi Initiative (DAY-NRLM)*: SHG capacity building, collateral-free loans up to ₹5,00,000.
  3. *Pradhan Mantri Ujjwala Yojana 2.0 (PMUY)*: Free deposit-free LPG gas connection + free 1st cylinder & stove.
  4. *Sukanya Samriddhi Yojana (SSY)*: 8.2% high compound interest savings for daughters under 10.
  5. *Pradhan Mantri Awas Yojana - Gramin (PMAY-G)*: ₹1,20,000 pucca house grant in woman's name.
  6. *Indira Gandhi National Widow Pension Scheme (IGNWPS)*: Monthly subsistence pension.
- **State-Specific Schemes**:
  7. *Tamil Nadu*: Kalaignar Magalir Urimai Thogai (₹1,000/month basic income for women heads of household).
  8. *Tamil Nadu*: Dr. Muthulakshmi Reddy Maternity Scheme (₹18,000 financial support + 2 Amma nutrition kits).
  9. *Andhra Pradesh*: YSR Cheyutha & Aasara (₹18,750/year for SC/ST/BC/Minority women aged 45-60).
  10. *Telangana*: Mahalakshmi Scheme (₹2,500/month + free TSRTC bus travel + ₹500 gas cylinder).
  11. *Kerala*: Kudumbashree Micro-Enterprise & Livelihood Scheme (Subsidized loans up to ₹10 Lakhs).
  12. *Madhya Pradesh*: Mukhyamantri Ladli Behna Yojana (₹1,250/month direct DBT).
  13. *Uttar Pradesh*: Mukhyamantri Kanya Sumangala Yojana (₹25,000 grant across 6 stages from birth to graduation).
  14. *Bihar*: Mukhyamantri Kanya Utthan Yojana (₹54,100 total grant up to graduation).

### 6. End-to-End Offline Submission Path
- Doesn't stop at "eligible".
- Guides woman through physical steps:
  - Explains how to link bank account with Aadhaar / NPCI mapping for DBT at the post office.
  - Generates token code (e.g., `VS-A49F21`).
  - Identifies physical submission center (Anganwadi center, Gram Panchayat Sachiv, Fair Price ration shop camp).

### 7. Privacy & Safety Protection (Discreet Use)
- **Earpiece Mode**: One-tap toggle that drops volume to 0.25 (whisper level) for private listening.
- **Quick Hang-up / Panic Camouflage**: Pressing `*` or clicking *"Quick Hang-up / Mausam"* instantly swaps screen and audio to **"Gramin Krishi Mausam Seva" (Rural Weather & Crop Advice)** or **"Desi Rasoi" (Kitchen Recipe)**, eliminating social friction or domestic surveillance.

---

## 🎨 Frontend Design Aesthetic

- **Color Palette**: Light greyish-white tones (`#f8fafc`, `#edf2f7`, `#ffffff`, `#e2e8f0`).
- **Glassmorphism**: Translucent frosted panels (`backdrop-filter: blur(18px)`), delicate borders, soft layered shadows.
- **Accessibility**: High-contrast typography, large tactile keypad buttons, live voice waveform animations, and multilingual font rendering.

---

## 🚀 Running the Application

### Prerequisites
- Python 3.10+
- Installed packages: `fastapi`, `uvicorn`, `pydantic`

### Starting the Server
From `d:\projects\VoiceSetu`:
```bash
python run.py
```
Open your browser at:
```
http://localhost:8000
```
