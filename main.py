from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    symptoms: str


@app.get("/")
def home():
    return {"message": "Jeevan Rakshak AI running 🚑"}


@app.post("/analyze")
def analyze(data: Input):

    text = data.symptoms.lower()

    # 🔴 CRITICAL (40+)
    critical_keywords = [
        # English
        "chest pain","heart attack","breathing difficulty","shortness of breath",
        "unconscious","fainting","severe bleeding","stroke","paralysis",
        "seizure","convulsion","cardiac arrest","blue lips","no pulse",
        "vomiting blood","coughing blood","head injury","fracture",
        "electric shock","burn severe","poison","overdose","suicide",
        "anaphylaxis","choking","internal bleeding","coma",
        "severe allergy","collapse",

        # Hindi
        "सीने में दर्द","दिल का दौरा","सांस लेने में दिक्कत","बेहोश",
        "खून बहना","लकवा","दौरा","नीले होंठ","नाड़ी नहीं",
        "खून की उल्टी","सिर की चोट","जहर","ओवरडोज",
        "आत्महत्या","घुटन","कोमा","गंभीर एलर्जी",

        # Gujarati
        "છાતીમાં દુખાવો","હાર્ટ એટેક","શ્વાસ લેવામાં તકલીફ","બેહોશ",
        "ખૂન વહેવું","લકવો","આંચકો","નીલા હોઠ","નાડી નથી",
        "ખૂન ની ઉલ્ટી","માથાની ઇજા","ઝેર","ઓવરડોઝ",
        "આત્મહત્યા","ઘૂંટણ","કોમા","ગંભીર એલર્જી"
    ]

    # 🟠 MODERATE (40+)
    moderate_keywords = [
        # English
        "fever","high fever","persistent fever","headache","migraine",
        "vomiting","nausea","diarrhea","stomach pain","abdominal pain",
        "back pain","joint pain","body pain","fatigue","weakness",
        "dizziness","cold","cough","sore throat","infection",
        "rash","swelling","burn minor","ear pain","tooth pain",
        "eye pain","blurred vision","urine infection",
        "dehydration","heatstroke","acidity","indigestion",
        "chills","loss of appetite",

        # Hindi
        "बुखार","तेज बुखार","सिरदर्द","उल्टी","मतली","दस्त",
        "पेट दर्द","कमर दर्द","जोड़ दर्द","थकान","कमजोरी",
        "चक्कर","खांसी","जुकाम","गले में दर्द","संक्रमण",
        "सूजन","जलन","कान दर्द","दांत दर्द","आंख दर्द",
        "धुंधला दिखना","पेशाब संक्रमण","डिहाइड्रेशन","गर्मी लगना",

        # Gujarati
        "તાવ","ઉંચો તાવ","માથાનો દુખાવો","ઉલ્ટી","મચકું","દસ્ત",
        "પેટ દુખાવો","કમર દુખાવો","સાંધાનો દુખાવો","થાક",
        "નબળાઈ","ચક્કર","ખાંસી","ઠંડી","ગળાનો દુખાવો",
        "ઇન્ફેક્શન","સૂજન","જલન","કાન દુખાવો","દાંત દુખાવો",
        "આંખ દુખાવો","ધૂંધળી દ્રષ્ટિ","મૂત્ર ચેપ","ડિહાઇડ્રેશન"
    ]

    # 🟢 MILD (30+)
    mild_keywords = [
        # English
        "tired","sleepy","stress","anxiety","minor cold","runny nose",
        "itching","dry skin","minor cut","small wound","mild headache",
        "light fever","seasonal allergy","gas","bloating","burping",

        # Hindi
        "थकान","नींद","तनाव","चिंता","हल्का जुकाम","नाक बहना",
        "खुजली","सूखी त्वचा","छोटा कट","हल्का बुखार",

        # Gujarati
        "થાક","ઊંઘ","તાણ","ચિંતા","હલકો તાવ","नाक વહેવું",
        "ખંજવાળ","સુકી ત્વચા","નાનો કટ","હલકો દુખાવો"
    ]

    # 🔴 CRITICAL RESPONSE
    for word in critical_keywords:
        if word in text:
            return {
                "level": "🚨 Critical",
                "advice": "Possible Condition: Life-threatening emergency\n\n"
                          "Advice:\nImmediate medical attention required.\n\n"
                          "Medicines:\nDo NOT self-medicate.\n\n"
                          "Precautions:\nRush to nearest hospital immediately.\n\n"
                          "⚠️ Do not take any medicine without consulting a doctor."
            }

    # 🟠 MODERATE RESPONSE
    for word in moderate_keywords:
        if word in text:
            return {
                "level": "⚠️ Moderate",
                "advice": "Possible Condition: Infection or illness\n\n"
                          "Advice:\nTake rest and stay hydrated.\n\n"
                          "Medicines:\nParacetamol, ORS\n\n"
                          "Precautions:\nMonitor symptoms carefully.\n\n"
                          "⚠️ Do not take any medicine without consulting a doctor."
            }

    # 🟢 MILD RESPONSE
    for word in mild_keywords:
        if word in text:
            return {
                "level": "✅ Mild",
                "advice": "Possible Condition: Minor issue\n\n"
                          "Advice:\nRest properly and maintain hydration.\n\n"
                          "Medicines:\nBasic home remedies\n\n"
                          "Precautions:\nMaintain healthy routine.\n\n"
                          "⚠️ Do not take any medicine without consulting a doctor."
            }

    # ❓ DEFAULT
    return {
        "level": "ℹ️ Unknown",
        "advice": "Condition unclear.\n\n⚠️ Consult a doctor before taking any medication."
    }
