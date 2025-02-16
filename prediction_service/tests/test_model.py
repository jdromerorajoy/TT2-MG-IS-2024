import pytest
from unittest.mock import patch, MagicMock
import torch
from app.model import predict_similarity

@patch("torch.load", return_value=MagicMock(predict=lambda x, target: torch.tensor([[0.8]])))
def test_predict_similarity(mock_model):
    tensor_1 = torch.tensor([[1, 2, 3]], dtype=torch.long)
    tensor_2 = torch.tensor([[0]], dtype=torch.long)
    prob = predict_similarity(tensor_1, tensor_2)
    assert 0 <= prob <= 1
