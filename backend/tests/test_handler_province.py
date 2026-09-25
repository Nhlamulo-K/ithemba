import json
from directory_api.handler import lambda_handler

def test_handler_echoes_the_province():
    event = {"queryStringParameters": {"province": "gauteng"}}
    result = lambda_handler(event, None)
    body = json.loads(result["body"])
    assert result["statusCode"] == 200
    assert body["province"] == "gauteng"

def test_handler_returns_services_for_a_province():
    event = {"queryStringParameters": {"province": "gauteng"}}
    response = lambda_handler(event, None)
    body = json.loads(response["body"])
    assert len(body["services"]) > 0
    for service in body["services"]:
        assert service["province"] in ("gauteng", "national")

def test_handler_returns_everything_when_no_province_given():
    event = {"queryStringParameters": {"province": None}}
    response = lambda_handler(event, None)
    body = json.loads(response["body"])
    assert body["province"] == None
    assert len(body["services"]) == 6