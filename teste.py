# Let's calculate the total estimated cost of the exams based on the average prices gathered.
exams_prices = {
    "Hemograma completo": 28,
    "Glicemia de jejum": 22,
    "Hemoglobina glicada": 30,  # approximate value based on similar tests
    "Colesterol total e frações": 66,
    "Triglicerídeos": 28,
    "Ureia": 28,
    "Creatinina": 28,
    "Sumário de urina com sedimentoscopia": 33,
    "Ácido úrico": 30,  # estimated
    "Hepatograma (TGO + TGP)": 54,  # sum of both TGO and TGP (27 each)
    "VDRL": 30,  # approximate value
    "HBsAG": 40,  # estimated
    "Anti-HBc": 40,  # estimated
    "Anti-HCV": 40,  # estimated
    "Anti-HBS": 40,  # estimated
    "T4 Livre": 60,
    "TSH": 59
}

# Summing the values to get the total estimated cost
total_cost = sum(exams_prices.values())
print(f"O valor total é: {total_cost}")
