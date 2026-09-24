"""Directory API Lambda handler (placeholder)."""
import json


def lambda_handler(event, context):
    # TODO: read services from DynamoDB, filter by province/type, return JSON
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"services": []}),
    }
