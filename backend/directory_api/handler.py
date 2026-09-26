"""Directory API Lambda handler (placeholder)."""
import json
from pathlib import Path
from directory_api.filtering import filter_by_province, filter_by_type
from directory_api.validate import valid_provinces, valid_types

def load_entries():
    path = Path(__file__).parent.parent.parent / "data" / "directory" / "services.json"
    return json.loads(path.read_text(encoding="utf-8"))

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    province = params.get("province")
    types = params.get("type")

    if province != None and province not in valid_provinces:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Unknown province"})
        }
    if types != None and types not in valid_types:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Unknown type"})
        }

    entries = load_entries()
    if province:
        entries = filter_by_province(entries, province)
    if types:
        entries = filter_by_type(entries, types)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"province": province, "type": types, "services": entries}),
    }
