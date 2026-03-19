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

    # 🔴 CRITICAL SYMPTOMS (EN + HI + GU)
    critical_keywords = [
        # English
        "chest pain", "heart attack", "breathing difficulty", "shortness of breath",
        "unconscious", "fainting", "severe bleeding", "stroke", "paralysis",
        "seizure", "cardiac arrest", "vomiting blood", "poison", "overdose",

        # Hindi
        "सीने में दर्द", "दिल का दौरा", "सांस लेने में दिक्कत",
        "बेहोश", "खून बहना", "लकवा", "दौरा", "जहर", "ओवरडोज",

        # Gujarati
        "છાતીમાં દુખાવો", "હાર્ટ એટેક", "શ્વાસ લેવામાં તકલીફ",
        "બેભાન", "રક્તસ્ત્રાવ", "લકવો", "ઝટકો", "ઝેર", "ઓવરડોઝ"
    ]

    # 🟠 MODERATE SYMPTOMS
    moderate_keywords = [
        # English
        "fever", "headache", "vomiting", "nausea", "diarrhea",
        "stomach pain", "back pain", "joint pain", "cough", "cold",
        "infection", "rash", "swelling", "eye pain", "tooth pain",

        # Hindi
        "बुखार", "सिर दर्द", "उल्टी", "मतली", "दस्त",
        "पेट दर्द", "कमर दर्द", "खांसी", "जुकाम", "संक्रमण",
        "सूजन", "आंख दर्द", "दांत दर्द",

        # Gujarati
        "તાવ", "માથાનો દુખાવો", "ઉલ્ટી", "મળમળ", "ડાયરીયા",
        "પેટમાં દુખાવો", "પીઠમાં દુખાવો", "ખાંસી", "ઠંડ",
        "સંક્રમણ", "સોજો", "આંખમાં દુખાવો", "દાંતમાં દુખાવો"
    ]

    # 🟢 MILD SYMPTOMS
    mild_keywords = [
        # English
        "tired", "mild headache", "sneezing", "runny nose",
        "itching", "minor cold", "stress", "anxiety",

        # Hindi
        "थकान", "हल्का सिर दर्द", "छींक", "नाक बहना",
        "खुजली", "तनाव", "चिंता",

        # Gujarati
        "થાક", "હળવો માથાનો દુખાવો", "છીંક", "નાક વહી",
        "ખંજવાળ", "તણાવ", "ચિંતા"
    ]

    # 🔴 CRITICAL CHECK
    for word in critical_keywords:
        if word in text:
            return {
                "level": "🚨 Critical",
                "advice": "Immediate medical attention required! Call ambulance or go to nearest hospital immediately."
            }

    # 🟠 MODERATE CHECK
    for word in moderate_keywords:
        if word in text:
            return {
                "level": "⚠️ Moderate",
                "advice": "Consult a doctor soon. Monitor symptoms and take proper rest."
            }

    # 🟢 MILD CHECK
    for word in mild_keywords:
        if word in text:
            return {
                "level": "✅ Mild",
                "advice": "Take rest, stay hydrated and monitor your condition."
            }

    # ❓ DEFAULT
    return {
        "level": "ℹ️ Unknown",
        "advice": "Symptoms unclear. Please consult a doctor."
    }
