import pytest
from app import predict_kidney_disease


# Define test cases
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ([120.0, 5.0, 8000], "No Chronic diseases"),
        ([140.0, 6.0, 7000], "The Person is suffering from Chronic disease"),
        # Add more test cases
        ([100.0, 4.0, 6000], "No Chronic diseases"),  # Lower values
        (
            [160.0, 7.0, 9000],
            "The Person is suffering from Chronic disease",
        ),  # Higher values
        ([130.0, 5.5, 7500], "No Chronic diseases"),  # Mid-range values
        (
            [110.0, 4.5, 8500],
            "The Person is suffering from Chronic disease",
        ),  # Mixed case
    ],
)
def test_prediction(input_data, expected_output):
    result = predict_kidney_disease(input_data)
    assert result == expected_output
