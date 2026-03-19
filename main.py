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

    # 🔴 CRITICAL (35+)
    critical_keywords = [
        # English
        "chest pain", "heart attack", "breathing difficulty", "shortness of breath",
        "unconscious", "fainting", "severe bleeding", "stroke", "paralysis",
        "seizure", "convulsion", "cardiac arrest", "blue lips", "no pulse",
        "vomiting blood", "coughing blood", "head injury", "fracture",
        "electric shock", "burn severe", "poison", "overdose", "suicide",
        "anaphylaxis", "choking", "severe pain", "internal bleeding",
        "collapsed", "coma", "severe allergy",

        # Hindi
        "सीने में दर्द", "दिल का दौरा", "सांस लेने में दिक्कत", "बेहोश",
        "खून बहना", "लकवा", "दौरा", "जहर", "ओवरडोज",
        "गंभीर दर्द", "सांस रुकना",

        # Gujarati
        "છાતીમાં દુખાવો", "હાર્ટ એટેક", "શ્વાસ લેવામાં તકલીફ", "બેભાન",
        "રક્તસ્ત્રાવ", "લકવો", "ઝટકો", "ઝેર", "ઓવરડોઝ",
        "ભારે દુખાવો", "શ્વાસ બંધ"
    ]

    # 🟠 MODERATE (40+)
    moderate_keywords = [
        # English
        "fever", "high fever", "persistent fever", "headache", "migraine",
        "vomiting", "nausea", "diarrhea", "stomach pain", "abdominal pain",
        "back pain", "joint pain", "body pain", "fatigue", "weakness",
        "dizziness", "cold", "cough", "sore throat", "infection",
        "rash", "swelling", "burn", "minor fracture", "ear pain",
        "tooth pain", "eye pain", "blurred vision", "urine infection",
        "dehydration", "heatstroke", "gas", "acidity", "indigestion",
        "chills", "body ache", "loss of appetite",

        # Hindi
        "बुखार", "सिर दर्द", "उल्टी", "मतली", "दस्त",
        "पेट दर्द", "कमर दर्द", "खांसी", "जुकाम", "संक्रमण",
        "सूजन", "आंख दर्द", "दांत दर्द", "चक्कर", "कमजोरी",
        "गैस", "अम्लता",

        # Gujarati
        "તાવ", "માથાનો દુખાવો", "ઉલ્ટી", "મળમળ", "ડાયરીયા",
        "પેટમાં દુખાવો", "પીઠમાં દુખાવો", "ખાંસી", "ઠંડ",
        "સંક્રમણ", "સોજો", "આંખમાં દુખાવો", "દાંતમાં દુખાવો",
        "ચક્કર", "નબળાઈ", "ગેસ", "એસિડિટી"
    ]

    # 🟢 MILD (30+)
    mild_keywords = [
        # English
        "tired", "slight fever", "mild headache", "sneezing", "runny nose",
        "itching", "minor cold", "light cough", "small cut", "bruise",
        "muscle soreness", "sleepy", "stress", "anxiety", "low energy",
        "dry skin", "hair fall", "minor swelling", "leg pain", "neck pain",

        # Hindi
        "थकान", "हल्का सिर दर्द", "छींक", "नाक बहना",
        "खुजली", "तनाव", "चिंता", "नींद आना",

        # Gujarati
        "થાક", "હળવો માથાનો દુખાવો", "છીંક", "નાક વહી",
        "ખંજવાળ", "તણાવ", "ચિંતા", "ઉંઘ"
    ]

    # 🔴 CRITICAL RESPONSE
    for word in critical_keywords:
        if word in text:
            return {
                "level": "🚨 Critical",
                "advice": """Possible Condition: Life-threatening emergency

Advice:
Immediate medical attention required.

Medicines:
Do NOT self-medicate.

Precautions:
Rush to nearest hospital immediately.

⚠️ Do not take any medicine without consulting a doctor."""
            }

    # 🟠 MODERATE RESPONSE
    for word in moderate_keywords:
        if word in text:
            return {
                "level": "⚠️ Moderate",
                "advice": """Possible Condition: Infection or illness

Advice:
Take rest and stay hydrated.

Medicines:
Paracetamol, ORS (basic support)

Precautions:
Monitor symptoms and consult doctor if condition worsens.

⚠️ Do not take any medicine without consulting a doctor."""
            }

    # 🟢 MILD RESPONSE
    for word in mild_keywords:
        if word in text:
            return {
                "level": "✅ Mild",
                "advice": """Possible Condition: Minor issue

Advice:
Rest properly and maintain hydration.

Medicines:
Home remedies or basic OTC care

Precautions:
Avoid stress and maintain healthy routine.

⚠️ Do not take any medicine without consulting a doctor."""
            }

    # ❓ DEFAULT
    return {
        "level": "ℹ️ Unknown",
        "advice": """Symptoms unclear.

Advice:
Consult a doctor for proper diagnosis.

⚠️ Do not take any medicine without consulting a doctor."""
    }
