from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from prediction import predict_match


app = FastAPI(
    title="PowerPlay AI API",
    description="IPL match winner prediction API using XGBoost",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MatchInput(BaseModel):
    team1: str
    team2: str
    venue: str
    toss_winner: str
    toss_decision: str
    match_total_runs: float
    total_wickets: float
    team_runs: float
    team_wicket: float


@app.get("/")
def home():
    return {
        "message": "PowerPlay AI Backend is running"
    }


@app.post("/predict")
def predict(input_data: MatchInput):
    result = predict_match(
        input_data.dict()
    )

    return result