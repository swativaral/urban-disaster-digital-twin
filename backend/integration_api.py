from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "project": "AI-Powered Urban Disaster Digital Twin",
        "module": "Integration API",
        "status": "running"
    })


@app.route("/predict-risk", methods=["POST"])
def predict_risk():
    data = request.get_json()

    rainfall = data.get("rainfall", 0)
    historical_flood = data.get("historical_flood", 0)

    if rainfall >= 200 or historical_flood == 1:
        risk_level = "CRITICAL"
        risk_score = 90
    elif rainfall >= 120:
        risk_level = "HIGH"
        risk_score = 70
    elif rainfall >= 60:
        risk_level = "MODERATE"
        risk_score = 45
    else:
        risk_level = "LOW"
        risk_score = 20

    return jsonify({
        "zone_id": data.get("zone_id"),
        "risk_score": risk_score,
        "risk_level": risk_level
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)
