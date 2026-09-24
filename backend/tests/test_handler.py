import json

from directory_api.handler import lambda_handler


def test_handler_returns_200():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200
    assert "services" in json.loads(response["body"])
