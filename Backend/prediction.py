
import joblib
import pandas as pd

from utils import (
    normalize_team_name,
    normalize_venue_name,
    get_city_from_venue,
    normalize_toss_decision
)

model = joblib.load("../models/powerplay_xgboost_model.pkl")
label_encoders = joblib.load("../models/label_encoders.pkl")
feature_cols = joblib.load("../models/feature_columns.pkl")
categorical_cols = joblib.load("../models/categorical_columns.pkl")


def prepare_input(data):
    venue = normalize_venue_name(data["venue"])
    city = get_city_from_venue(venue)

    input_data = {
        "team1": normalize_team_name(data["team1"]),
        "team2": normalize_team_name(data["team2"]),
        "venue": venue,
        "city": city,
        "toss_winner": normalize_team_name(data["toss_winner"]),
        "toss_decision": normalize_toss_decision(data["toss_decision"]),
        "stage": "Unknown",
        "match_total_runs": data["match_total_runs"],
        "batter_total_runs": data["match_total_runs"] * 0.94,
        "extra_total_runs": data["match_total_runs"] * 0.06,
        "total_wickets": data["total_wickets"],
        "team_runs": data["team_runs"],
        "team_balls": 120,
        "team_wicket": data["team_wicket"],
        "run_rate": data["match_total_runs"] / 40,
        "extras_percentage": 0.06
    }

    df = pd.DataFrame([input_data])

    for col in categorical_cols:
        df[col] = label_encoders[col].transform(df[col].astype(str))

    return df[feature_cols]


def predict_match(data):
    processed_df = prepare_input(data)

    probability = model.predict_proba(processed_df)[0][1]

    predicted_winner = (
        data["team1"]
        if probability >= 0.5
        else data["team2"]
    )

    return {
        "predicted_winner": str(predicted_winner),
        "team1_win_probability": float(round(float(probability) * 100, 2)),
        "team2_win_probability": float(round((1 - float(probability)) * 100, 2))
    }