from backend.ayurveda_data import AYURVEDA_DB

def find_disease_recommendation(disease_name):

    disease_name = disease_name.lower()

    for rec in AYURVEDA_DB:
        if disease_name in rec["disease"].lower():
            return rec

    return None