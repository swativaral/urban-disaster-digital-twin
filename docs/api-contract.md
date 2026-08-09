# API Contract

## 1. Purpose

This document defines the communication format between the
AI/ML, Backend, Routing, GIS and Frontend modules.

---

# 2. Risk Prediction API

## Endpoint

POST /predict-risk

## Purpose

Predict the disaster risk level of a specific zone.

## Request

```json
{
  "zone_id": "Z01",
  "rainfall": 180,
  "elevation": 42,
  "slope": 2.1,
  "drainage": 0.35,
  "distance_from_water": 0.8,
  "historical_flood": 1
}
Response
{
  "zone_id": "Z01",
  "risk_score": 87,
  "risk_level": "CRITICAL"
}
3. Citizen Safe Route API
Endpoint

POST /citizen-route

Purpose

Find the safest available route for a citizen.

Request
{
  "source": "LOC01",
  "destination": "S01"
}
Response
{
  "source": "LOC01",
  "destination": "S01",
  "route": ["R01", "R04", "R09"],
  "eta_minutes": 10,
  "risk_score": 15,
  "route_status": "SAFE"
}
4. Ambulance Route API
Endpoint

POST /ambulance-route

Purpose

Find the safest and fastest route for an ambulance.

Request
{
  "ambulance_id": "A01",
  "incident_id": "INC01",
  "destination_type": "HOSPITAL"
}
Response
{
  "ambulance_id": "A01",
  "incident_id": "INC01",
  "hospital_id": "H02",
  "route": ["R01", "R05", "R08"],
  "eta_minutes": 9,
  "route_risk": 12,
  "route_status": "SAFE"
}
5. Hospital Recommendation API
Endpoint

POST /recommend-hospital

Purpose

Recommend a suitable hospital based on distance, risk and availability.

Request
{
  "incident_id": "INC01",
  "latitude": 18.5204,
  "longitude": 73.8567
}
Response
{
  "hospital_id": "H02",
  "hospital_name": "Hospital B",
  "distance_km": 3.2,
  "eta_minutes": 9,
  "available_capacity": 60,
  "risk_score": 12
}
6. Shelter Recommendation API
Endpoint

POST /recommend-shelter

Purpose

Recommend a safe nearby shelter.

Request
{
  "zone_id": "Z01",
  "latitude": 18.5204,
  "longitude": 73.8567
}
Response
{
  "shelter_id": "S01",
  "shelter_name": "Shelter A",
  "distance_km": 2.1,
  "eta_minutes": 7,
  "available_capacity": 120,
  "risk_score": 8
}
7. Disaster Simulation API
Endpoint

POST /simulate

Purpose

Simulate disaster conditions and observe their effect on
risk levels, affected zones and routes.

Request
{
  "rainfall": 220,
  "blocked_roads": ["R17", "R21"]
}
Response
{
  "simulation_id": "SIM01",
  "affected_zones": ["Z01", "Z03"],
  "critical_zones": ["Z01"],
  "blocked_roads": ["R17", "R21"],
  "rerouting_required": true
}
8. Dynamic Re-routing API
Endpoint

POST /reroute

Purpose

Generate a new route when the current route becomes unsafe
or blocked.

Request
{
  "current_route": ["R01", "R04", "R09"],
  "blocked_roads": ["R04"],
  "destination": "H02"
}
Response
{
  "new_route": ["R01", "R06", "R09"],
  "eta_minutes": 11,
  "route_risk": 14,
  "route_status": "SAFE"
}
9. Zone Information API
Endpoint

GET /zones

Purpose

Retrieve disaster risk information for all monitored zones.

Response
{
  "zones": [
    {
      "zone_id": "Z01",
      "risk_score": 87,
      "risk_level": "CRITICAL"
    },
    {
      "zone_id": "Z02",
      "risk_score": 35,
      "risk_level": "MODERATE"
    }
  ]
}
10. Road Status API
Endpoint

GET /roads

Purpose

Retrieve current road conditions for routing.

Response
{
  "roads": [
    {
      "road_id": "R01",
      "status": "OPEN",
      "risk_score": 10
    },
    {
      "road_id": "R17",
      "status": "BLOCKED",
      "risk_score": 95
    }
  ]
}
11. Emergency Alert API
Endpoint

POST /send-alert

Purpose

Generate an early disaster warning for users in affected zones.

Request
{
  "zone_id": "Z01",
  "risk_level": "CRITICAL",
  "message": "Severe flood risk detected. Move to a safe shelter."
}
Response
{
  "alert_id": "ALT01",
  "zone_id": "Z01",
  "status": "SENT"
}
12. Common Status Values
Risk Levels
LOW
MODERATE
HIGH
CRITICAL
Road Status
OPEN
HIGH_RISK
BLOCKED
Route Status
SAFE
MODERATE
HIGH_RISK
UNAVAILABLE
Alert Status
PENDING
SENT
FAILED
13. Common Entity IDs

Zones:

Z01
Z02
Z03

Roads:

R01
R02
R03

Hospitals:

H01
H02
H03

Shelters:

S01
S02
S03

Ambulances:

A01
A02
A03

Incidents:

INC01
INC02
INC03
14. Integration Flow

Weather / Historical / GIS Data
↓
AI/ML Risk Prediction
↓
Risk Score
↓
Backend
↓
Routing Engine
↓
Citizen / Ambulance Route
↓
Hospital / Shelter Recommendation
↓
Dynamic Re-routing
↓
Frontend Dashboard
↓
Emergency Alert

15. Module Dependencies

AI/ML → Backend

GIS → Backend

GIS → Routing

AI/ML → Routing

Backend → Routing

Backend → Frontend

Routing → Backend

Backend → Frontend

16. Integration Principle

All modules must use the same entity IDs, request formats,
response formats and status values defined in this document.

Any change to an API request or response must be updated in
this document before integration.
