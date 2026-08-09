# Integration Test Cases

## 1. Purpose

This document defines test cases for validating the integration
between AI/ML, GIS, Routing, Backend and Frontend modules.

---

# 2. Risk Prediction Tests

## TEST-01: Low Risk Zone

### Input

- Rainfall: Low
- Historical flood: 0
- Good drainage

### Expected Result

- Risk score should be low.
- Risk level should be LOW.

---

## TEST-02: High Risk Zone

### Input

- Heavy rainfall
- Poor drainage
- Historical flood: 1

### Expected Result

- Risk score should increase.
- Risk level should be HIGH or CRITICAL.

---

## TEST-03: Critical Risk Zone

### Input

- Very heavy rainfall
- Poor drainage
- Low elevation
- Historical flood: 1

### Expected Result

- Risk level should be CRITICAL.
- Early warning should be generated.

---

# 3. Routing Tests

## TEST-04: Safe Route

### Input

- Source: LOC01
- Destination: S01
- All roads available

### Expected Result

- A valid route should be generated.
- Route should contain road IDs.
- ETA should be returned.

---

## TEST-05: Blocked Road

### Input

- Current route contains R17.
- R17 status = BLOCKED.

### Expected Result

- R17 should not be used.
- Alternative route should be generated.

---

## TEST-06: High Risk Road

### Input

- R17 status = HIGH_RISK.
- Alternative safe road is available.

### Expected Result

- Routing engine should prefer the safer alternative.
- Route risk should be reduced.

---

# 4. Ambulance Tests

## TEST-07: Ambulance Route

### Input

- Ambulance: A01
- Incident: INC01
- Hospital: H02

### Expected Result

- Fast and safe route should be generated.
- ETA should be returned.
- Route risk should be returned.

---

## TEST-08: Hospital Unavailable

### Input

- Hospital H01 status = FULL.
- Hospital H02 status = AVAILABLE.

### Expected Result

- H01 should not be selected.
- H02 should be recommended.

---

# 5. Shelter Tests

## TEST-09: Safe Shelter Recommendation

### Input

- Zone: Z01
- Multiple shelters available.

### Expected Result

- Nearby safe shelter should be recommended.
- Available capacity should be displayed.

---

## TEST-10: Unsafe Shelter

### Input

- Shelter S01 has high risk.
- Shelter S02 is safe.

### Expected Result

- S01 should be avoided.
- S02 should be recommended.

---

# 6. Dynamic Re-routing Tests

## TEST-11: Route Becomes Blocked

### Input

- Current route: R01 → R04 → R09
- R04 becomes BLOCKED.

### Expected Result

- System should detect the blocked road.
- New route should be generated.
- New ETA should be returned.

---

## TEST-12: Route Risk Increases

### Input

- Current route risk increases significantly.

### Expected Result

- System should identify the route as HIGH_RISK.
- Alternative route should be considered.

---

# 7. Disaster Simulation Tests

## TEST-13: Rainfall Increase

### Input

- Rainfall increases from normal to heavy.

### Expected Result

- Risk scores should be recalculated.
- Affected zones should be identified.
- Risk levels should update.

---

## TEST-14: Multiple Road Blockage

### Input

- R17 and R21 become BLOCKED.

### Expected Result

- Affected routes should be recalculated.
- Alternative routes should be generated where possible.

---

# 8. Emergency Alert Tests

## TEST-15: Critical Alert

### Input

- Zone Z01 risk level = CRITICAL.

### Expected Result

- Emergency alert should be generated.
- Alert should contain zone information.
- Alert status should be SENT.

---

## TEST-16: Moderate Risk

### Input

- Zone Z02 risk level = MODERATE.

### Expected Result

- No critical emergency alert should be generated.
- Risk information should be visible on the dashboard.

---

# 9. Integration Tests

## TEST-17: ML to Backend

### Input

ML generates:

- zone_id = Z01
- risk_score = 87
- risk_level = CRITICAL

### Expected Result

- Backend should receive and store the prediction correctly.

---

## TEST-18: Backend to Routing

### Input

- Road risk information from Backend.

### Expected Result

- Routing engine should use the latest risk information.

---

## TEST-19: Backend to Frontend

### Input

- Risk and route data from Backend.

### Expected Result

- Frontend should display:
  - Risk level
  - Risk score
  - Route
  - ETA
  - Road status

---

## TEST-20: End-to-End Disaster Scenario

### Scenario

Heavy rainfall causes flooding in Zone Z01.

### Expected Flow

Weather Data
↓
AI/ML Risk Prediction
↓
Critical Risk Detected
↓
Emergency Alert
↓
Affected Roads Identified
↓
Safe Route Calculated
↓
Shelter/Hospital Recommended
↓
Frontend Dashboard Updated

### Expected Result

The complete disaster-response workflow should execute
without integration errors.

---

# 10. Test Status

Each test case should be marked as:

- NOT STARTED
- IN PROGRESS
- PASSED
- FAILED
- BLOCKED

---

# 11. Testing Rule

A test is considered PASSED only when the actual output
matches the expected output.

Any failed test must be documented and assigned to the
responsible module member.
