import json
from pathlib import Path

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


@app.get("/points-table")
def get_points_table():
    file_path = Path(__file__).parent / "DATA" / "points_table.json"

    with open(file_path, "r", encoding="utf-8") as file:
        points_table = json.load(file)

    return {
        "points_table": points_table
    }


@app.post("/predict")
def predict(input_data: MatchInput):
    result = predict_match(
        input_data.dict()
    )

    return result