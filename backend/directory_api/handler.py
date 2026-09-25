"""Directory API Lambda handler (placeholder)."""
import json
from pathlib import Path
from directory_api.filtering import filter_by_province, filter_by_type

def load_entries():
    path = Path(__file__).parent.parent.parent / "data" / "directory" / "services.json"
    return json.loads(path.read_text(encoding="utf-8"))

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    province = params.get("province")
    types = params.get("type")

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
