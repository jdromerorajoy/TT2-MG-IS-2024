import pytest
from unittest.mock import patch
from app.services import PredictionClient

@patch("requests.post")
def test_get_prediction(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"prediction": 0.85}

    inputs = [["data1"], ["data2"]]
    result = PredictionClient.get_prediction(inputs)

    assert result == {"prediction": 0.85}
    mock_post.assert_called_once()
