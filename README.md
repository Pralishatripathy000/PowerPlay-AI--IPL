<img width="1568" height="754" alt="image" src="https://github.com/user-attachments/assets/de5e1ff2-0e9c-4172-a821-b47f39ae5c73" />

<div align="center">

# 🏏 PowerPlay AI

## AI-Powered IPL Match Winner Prediction



*AI-powered IPL analytics and match winner prediction • Ball-by-ball data • Live from the stadium*

<br/>

[🚀 Live Demo](https://id-preview--60d71c7e-16ab-4bfb-a9ca-c63c34731357.lovable.app/) &nbsp;•&nbsp; [📖 API Docs](#backend--api) &nbsp;•&nbsp; [📊 Model Details](#model-details)

</div>

---

## 📌 Overview

**PowerPlay AI** is an end-to-end machine learning sports analytics system that predicts IPL match winners using historical ball-by-ball IPL data (2008–2025), engineered match-level features, and gradient-boosting models (XGBoost & CatBoost). The project includes a production-ready **FastAPI backend** and a **Lovable/React dashboard** for real-time prediction display.

> 🎯 **Tap the button — our AI crunches form, NRR and momentum to crown the champion.**

---

## 🔍 What Makes PowerPlay AI Different?

Most IPL prediction projects available online follow a similar, simplified pattern — feed team names, toss result, and venue into a basic classifier and call it done. PowerPlay AI was designed with a fundamentally different philosophy.

### ❌ What typical IPL ML projects do

```
team1 + team2 + venue + toss_winner  →  basic classifier  →  win/loss
```

Usually built on Logistic Regression or Random Forest, evaluated only on historical accuracy, with no external season validation.

### ✅ What PowerPlay AI does differently

**1. Ball-by-ball → Match Intelligence**
Rather than using surface-level inputs, the entire 283,678-row ball-by-ball dataset was transformed into structured match-level analytical features that actually reflect *how* T20 games are won — capturing run rate, wicket pressure, batter contribution, extras load, innings-based momentum, and team scoring patterns.

**2. Real External Validation**
The model was validated on a completely separate IPL 2026 dataset (39 unseen matches) — a dataset that never touched the training pipeline. This directly addresses the overfitting problem common in most IPL ML projects, where models score 95%+ on historical splits but fail on new seasons.

**3. Advanced Boosting Models**
XGBoost and CatBoost were compared against each other — not just basic algorithms — and the final model was selected based on both historical accuracy *and* 2026 generalization performance.

**4. Production Architecture, Not Just a Notebook**
The system includes a FastAPI backend with a `/predict` REST endpoint, model serialization via Joblib, and a live React/Lovable dashboard — making it a deployable sports analytics product, not just a Jupyter experiment.

💡 The 2026 external test used an incomplete dataset (39 matches, limited depth compared to the ball-by-ball training data). The model's engineered features depend on rich ball-by-ball inputs — when those are shallow, predictions naturally drop. The 92% historical accuracy on the full dataset is the more representative benchmark. The 2026 test was included purely for real-world generalization transparency, not as the primary evaluation.

### 💛 Built with Cricket Passion

This project was also built out of genuine love for IPL and cricket. As an RCB fan, the idea started as a fun side project to explore how machine learning could interpret match momentum and pressure in one of the most unpredictable T20 leagues in the world. With the **IPL Final on 31 May**, the timing felt perfect to blend cricket excitement with real ML engineering.

---

## ✨ Features

- 🏆 **Champion Prediction** — predicts the IPL season winner with confidence scores
- 🔮 **Match Winner Prediction** — head-to-head match outcome prediction with win probabilities
- 📊 **EDA & Feature Engineering** — ball-by-ball data aggregated into match-level features
- 🤖 **Dual Model Comparison** — XGBoost vs CatBoost with external season validation
- ⚡ **FastAPI Backend** — `/predict` REST endpoint with JSON probability output
- 🖥️ **React Dashboard** — live Lovable/React UI for prediction display
- 🚀 **Deployment Ready** — configured for Render / Railway deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Data Processing** | Python, Pandas, NumPy |
| **Visualization** | Matplotlib |
| **ML Models** | Scikit-learn, XGBoost, CatBoost |
| **Model Serialization** | Joblib |
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | React / Lovable |
| **Version Control** | Git & GitHub |
| **Deployment** | Render / Railway |

---

## 📂 Project Structure

```
powerplay-ipl/
│
├── data/
│   ├── IPL.csv                          # Primary dataset (283,678 rows, ball-by-ball)
│   └── ipl_2026_match39_dataset.csv     # External test dataset (IPL 2026)
│
├── notebooks/
│   ├── 01_eda.ipynb                     # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb     # Feature engineering pipeline
│   └── 03_modelling.ipynb               # Model training & comparison
│
├── models/
│   ├── powerplay_xgboost_model.pkl      # Final production model
│   ├── label_encoders.pkl               # Categorical encoders
│   ├── feature_columns.pkl              # Feature schema
│   └── categorical_columns.pkl          # Categorical column list
│
├── api/
│   ├── main.py                          # FastAPI application
│   └── predictor.py                     # Prediction logic
│
├── frontend/                            # React / Lovable dashboard
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Details

### Primary Dataset — `IPL.csv`

| Property | Value |
|----------|-------|
| **Seasons** | 2008 – 2025 |
| **Total Rows** | 283,678 |
| **Columns** | 65 |
| **Granularity** | Ball-by-ball |

**Key columns used:**

```
match_id        season          venue           city
batting_team    bowling_team    toss_winner     toss_decision
match_won_by    runs_total      runs_batter     runs_extras
bowler_wicket   team_runs       team_balls      team_wicket
valid_ball      stage
```

### External Test Dataset — `ipl_2026_match39_dataset.csv`

| Property | Value |
|----------|-------|
| **Season** | IPL 2026 |
| **Matches** | 39 |
| **Purpose** | External validation only (not used in training) |

---

## ⚙️ Feature Engineering

The ball-by-ball dataset was aggregated into a **match-level dataset** using `match_id`.

**Engineered features:**

| Feature | Description |
|---------|-------------|
| `team1`, `team2` | Teams playing the match |
| `venue`, `city` | Match location |
| `toss_winner`, `toss_decision` | Toss outcome |
| `stage` | Tournament stage (group / playoff / final) |
| `match_total_runs` | Total runs in the match |
| `batter_total_runs` | Total batter runs |
| `extra_total_runs` | Total extra runs |
| `total_wickets` | Wickets fallen |
| `team_runs`, `team_balls`, `team_wicket` | Innings-level aggregates |
| `run_rate` | Runs per over |
| `extras_percentage` | Proportion of extras |

**Target Variable:**

```
team1_win   →   1 = team1 won   |   0 = team2 won
```

---

## 🤖 Model Details

### XGBoost Classifier ✅ *(Final Model)*

```python
Model:      XGBClassifier
Training:   IPL 2008–2025
Validation: Train-test split
External:   IPL 2026 match data
```

| Metric | Score |
|--------|-------|
| Historical Test Accuracy | **91.45%** |
| 2026 External Accuracy | **61.54%** |

### CatBoost Classifier *(Comparison)*

```python
Model:   CatBoostClassifier
Note:    Handles categorical features natively
Usage:   Model comparison with XGBoost
```

| Metric | Score |
|--------|-------|
| Historical Test Accuracy | **91.03%** |
| 2026 External Accuracy | **56.41%** |

### Why XGBoost?

XGBoost was selected as the final model because it outperformed CatBoost on both historical test data *and* unseen 2026 external data, demonstrating better generalization to new seasons.

---

## ⚡ Backend & API

The FastAPI backend exposes a `/predict` endpoint that accepts match parameters and returns prediction probabilities.

### Running the API

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn api.main:app --reload
```

### `/predict` Endpoint

**Request:**

```json
{
  "team1": "Royal Challengers Bengaluru",
  "team2": "Punjab Kings",
  "venue": "M. Chinnaswamy Stadium",
  "city": "Bengaluru",
  "toss_winner": "Royal Challengers Bengaluru",
  "toss_decision": "bat",
  "stage": "Final"
}
```

**Response:**

```json
{
  "predicted_winner": "Royal Challengers Bengaluru",
  "team1_win_probability": 75.73,
  "team2_win_probability": 24.27
}
```

Interactive API docs available at `http://localhost:8000/docs` (Swagger UI).

---

## 🖥️ Dashboard

The React/Lovable frontend dashboard provides:

- **Season Finale Prediction** — AI-powered champion prediction with confidence score
- **Runner-up Prediction** — second-place team prediction
- **Live Mock Data** toggle
- **Historical seasons** selector (2008–2026)

🔗 **[View Live Dashboard →](https://id-preview--60d71c7e-16ab-4bfb-a9ca-c63c34731357.lovable.app/)**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/powerplay-ipl.git
cd powerplay-ipl
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run notebooks (in order)

```bash
jupyter notebook notebooks/01_eda.ipynb
jupyter notebook notebooks/02_feature_engineering.ipynb
jupyter notebook notebooks/03_modelling.ipynb
```

### 4. Start the API

```bash
uvicorn api.main:app --reload --port 8000
```

### 5. Open the dashboard

Visit the [Live Demo](https://id-preview--60d71c7e-16ab-4bfb-a9ca-c63c34731357.lovable.app/) or run the React app locally.

---

## 📦 Requirements

```
pandas
numpy
matplotlib
scikit-learn
xgboost
catboost
joblib
fastapi
uvicorn
```

---

## 📈 Results Summary

| Model | Historical Accuracy | 2026 External Accuracy |
|-------|--------------------|-----------------------|
| XGBoost ✅ | **91.45%** | **61.54%** |
| CatBoost | 91.03% | 56.41% |

> 💡 The drop in 2026 accuracy (vs historical) is expected — new seasons introduce unseen team compositions, player transfers, and match dynamics. 61.54% on completely unseen data is a solid generalization benchmark.

---

## 🗺️ Project Outcomes

PowerPlay AI is a deployable machine learning sports analytics project combining:

- ✅ Exploratory Data Analysis (EDA)
- ✅ Feature Engineering (ball-by-ball → match-level)
- ✅ XGBoost Modelling
- ✅ CatBoost Comparison
- ✅ External Season Validation (IPL 2026)
- ✅ FastAPI Backend
- ✅ Lovable/React Dashboard
- ✅ Deployment-ready Architecture

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ and 🏏 for IPL fans everywhere

**PowerPlay • Play • IPL!**

</div>
