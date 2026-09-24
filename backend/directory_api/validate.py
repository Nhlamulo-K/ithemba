import json
from pathlib import Path
import re
import sys

path = Path("../data/directory/services.json")
entries = json.loads(path.read_text(encoding="utf-8"))

# print(f"{len(entries)} entries loaded")
# for entry in entries:
#     print(entry["name"], "-", entry["phone"])

required_fields = ["id", "name", "type", "province", "phone", "source_url", "last_verified"]
valid_types = ["helpline", "police", "thuthuzela", "shelter", "legal", "clinic"]
valid_provinces = ["national", "eastern-cape", "free-state", "gauteng", "kwazulu-natal",
                    "limpopo", "mpumalanga", "northern-cape", "north-west", "western-cape"]
phone_numbers = re.compile(r"^[0-9*#+() -]{3,25}$")

def validate_entries(entries):
    problems =[]

    for entry in entries:
        for field in required_fields:
            if not entry.get(field):
                problems.append(f"{entry.get('id', 'unknown')}: missing '{field}'")
        if entry.get("type") and entry["type"] not in valid_types:
            problems.append(f"{entry.get('id', 'unknown')}: unknown type '{entry['type']}'")
        if entry.get("province") and entry["province"] not in valid_provinces:
            problems.append(f"{entry.get('id', 'unknown')}: unknown province '{entry['province']}'")
        if entry.get("phone") and not phone_numbers.match(entry.get("phone")):
            problems.append(f"{entry.get('id', 'unknown')}: phone '{entry.get("phone")}' has an unexpected format")
        
        return problems

if __name__ =="__main__":
    print(f"{len(entries)} entries checked")

    problems = validate_entries(entries)

    for problem in problems:
        print("PROBLEM:", problem)
    print(f"{len(problems)} problem(s) found")
    sys.exit(1 if problems else 0)