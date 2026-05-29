import pytest
import pandas as pd
from unittest.mock import patch
from whocausal.loader import WHODataloader

# Fixture for providing a mock WHO API response
@pytest.fixture
def mock_who_response():
    return {
        "value": [
            # Valid contries
            {"SpatialDim": "DEU", "TimeDim": 2020, "NumericValue": "22.5"},
            {"SpatialDim": "FRA", "TimeDim": 2020, "NumericValue": "21.0"},

            # Region GLOBAL should be filtered out
            {"SpatialDim": "GLOBAL", "TimeDim": 2020, "NumericValue": "20.0"} 
        ]
    }

# Decorator patch intercepts the real requests.get and replaces it with a mock (mock_get)
@patch('whocausal.loader.requests.get')
def test_fetch_indicator_success(mock_get, mock_who_response):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_who_response

    loader = WHODataloader()
    df = loader.fetch_indicator("TEST_IND")

    assert len(df) == 2, "Expected 2 rows, as GLOBAL should be filtered out"
    assert "country_code" in df.columns, "Country column not renamed"
    assert "test_ind" in df.columns, "Value column not renamed to lowercase"
    assert df.iloc[0]["country_code"] == "DEU"
    assert df.iloc[0]["test_ind"] == 22.5