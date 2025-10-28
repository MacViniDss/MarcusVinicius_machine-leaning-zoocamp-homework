import pickle

# Carregar o pipeline
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Novo lead para scoring
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Fazer a previsão (probabilidade)
# O predict_proba retorna as probabilidades para a classe 0 (não converte) e classe 1 (converte)
# Queremos a probabilidade de conversão (índice 1)
X = [record]
probability = pipeline.predict_proba(X)[0, 1]

print(f"Probabilidade de conversão: {probability:.3f}")
