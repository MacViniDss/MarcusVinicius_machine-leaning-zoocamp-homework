import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 1. Carregar o Pipeline
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# 2. Definir o esquema de entrada (para validação)
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

app = FastAPI()

@app.post("/predict")
def predict(lead: Lead):
    lead_dict = lead.dict() 
    
    # Fazer a previsão
    X = [lead_dict]
    # Pega a probabilidade da classe positiva (índice 1)
    probability = pipeline.predict_proba(X)[0, 1]
    
    return {"probability": float(f"{probability:.3f}")}

if __name__ == "__main__":
    pass
