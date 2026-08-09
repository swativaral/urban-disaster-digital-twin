# API Contract

## 1. Purpose

This document defines the communication format between the
AI/ML, Backend, Routing and Frontend modules.

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
