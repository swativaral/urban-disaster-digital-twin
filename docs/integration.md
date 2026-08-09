# System Integration Specification

## 1. Project

AI-Powered Urban Disaster Early Warning & Emergency Response Digital Twin

## 2. Integration Objective

The objective is to integrate AI/ML, GIS, Routing, Backend and
Frontend modules into a single disaster-response system.

## 3. System Flow

Weather / Historical / GIS Data
            ↓
       AI/ML Model
            ↓
      Flood Risk Score
            ↓
         Database
            ↓
      Routing Engine
            ↓
   ┌────────┴────────┐
   ↓                 ↓
Citizen           Ambulance
Route              Route
   ↓                 ↓
Shelter           Hospital
   └────────┬────────┘
            ↓
      Dynamic Re-routing
            ↓
       Frontend Dashboard

## 4. Module Responsibilities

### AI/ML
Input:
- Rainfall
- Elevation
- Slope
- Drainage
- Distance from water
- Historical flood data

Output:
- Zone ID
- Risk Score
- Risk Level

### GIS
Input:
- Geographic datasets

Output:
- Roads
- Zones
- Hospitals
- Shelters
- Water bodies

### Routing
Input:
- Road network
- Travel time
- Flood risk
- Road status

Output:
- Route
- ETA
- Route risk

### Backend
Input:
- ML data
- GIS data
- Routing data

Output:
- APIs for frontend

### Frontend
Input:
- Backend API responses

Output:
- Map
- Risk visualization
- Alerts
- Routes
- Hospital/Shelter information

## 5. Integration Dependencies

AI/ML → Backend → Routing → Frontend

GIS → Backend → Routing

AI/ML risk scores are used by the routing engine to calculate
risk-aware routes.

## 6. Common Entity IDs

Zones: Z01, Z02, Z03

Roads: R01, R02, R03

Hospitals: H01, H02, H03

Shelters: S01, S02, S03

Ambulances: A01, A02, A03

Incidents: INC01, INC02, INC03
