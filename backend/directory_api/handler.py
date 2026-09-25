"""Directory API Lambda handler (placeholder)."""
import json
from pathlib import Path
from directory_api.filtering import filter_by_province

def load_entries():
    path = Path(__file__).parent.parent.parent / "data" / "directory" / "services.json"
    return json.loads(path.read_text(encoding="utf-8"))

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    province = params.get("province")

    entries = load_entries()
    if province:
        entries = filter_by_province(entries, province)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"province": province, "services": entries}),
    }
