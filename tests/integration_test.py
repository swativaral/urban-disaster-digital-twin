import unittest
import json

from backend.integration_api import app


class IntegrationAPITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(data["status"], "healthy")

    def test_risk_prediction(self):
        payload = {
            "zone_id": "Z01",
            "rainfall": 220,
            "historical_flood": 1
        }

        response = self.client.post(
            "/predict-risk",
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(data["zone_id"], "Z01")
        self.assertEqual(data["risk_level"], "CRITICAL")
        self.assertGreaterEqual(data["risk_score"], 0)
        self.assertLessEqual(data["risk_score"], 100)


if __name__ == "__main__":
    unittest.main()
