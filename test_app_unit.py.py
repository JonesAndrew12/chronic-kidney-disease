# test_app_unit.py

import unittest
from app import predict_kidney_disease, is_valid_input


class TestKidneyDiseasePredictionUnit(unittest.TestCase):
    def test_is_valid_input_valid(self):
        # Test case with valid input

        result = is_valid_input(123)
        self.assertTrue(result)

    def test_is_valid_input_invalid(self):
        # Test case with invalid input
        result = is_valid_input("abc")
        self.assertFalse(result)

    def test_predict_kidney_disease_chronic(self):
        # Test CKD prediction for chronic disease
        result = predict_kidney_disease(140, 5, 9000)
        self.assertEqual(result, "The Person is suffering from Chronic disease")

    def test_predict_kidney_disease_no_chronic(self):
        # Test CKD prediction for no chronic disease
        result = predict_kidney_disease(120, 6, 7000)
        self.assertEqual(result, "No Chronic diseases")

    # Add more unit test cases as needed


if __name__ == "__main__":
    unittest.main()
