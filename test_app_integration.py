# test_app_integration.py

import unittest
from app import integrated_prediction


class TestKidneyDiseasePredictionIntegration(unittest.TestCase):
    def test_integrated_prediction_chronic(self):
        # Test integrated prediction for chronic disease
        result = integrated_prediction(140, 5, 9000)
        self.assertEqual(result, "The Person is suffering from Chronic disease")

    def test_integrated_prediction_no_chronic(self):
        # Test integrated prediction for no chronic disease
        result = integrated_prediction(120, 6, 7000)
        self.assertEqual(result, "No Chronic diseases")

    # Add more integrated test cases as needed


if __name__ == "__main__":
    unittest.main()
