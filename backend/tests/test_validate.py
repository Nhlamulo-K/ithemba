from directory_api.validate import validate_entries

GOOD_ENTRY = {
    "id": "gbv-command-centre",
    "name": "GBV Command Centre",
    "type": "helpline",
    "province": "national",
    "phone": "0800 428 428",
    "source_url": "https://sanews.gov.za/node/61236",
    "last_verified": "2026-09-24",
}


def test_good_entry_has_no_problems():
    assert validate_entries([GOOD_ENTRY]) == []

def test_missing_phone_is_reported():
    entry = dict(GOOD_ENTRY)
    del entry["phone"]
    problems = validate_entries([entry])
    assert problems == ["gbv-command-centre: missing 'phone'"]

def test_unknown_type_is_reported():
    entry = dict(GOOD_ENTRY)
    entry["type"] = "club"
    problems = validate_entries([entry])
    assert problems == ["gbv-command-centre: unknown type 'club'"]

def test_unknown_province_is_reported():
    entry = dict(GOOD_ENTRY)
    entry["province"] = "lesotho"
    problems = validate_entries([entry])
    assert problems == ["gbv-command-centre: unknown province 'lesotho'"]

def test_bad_phone_is_reported():
    entry = dict(GOOD_ENTRY)
    entry["phone"] = "call me"
    problems = validate_entries([entry])
    assert problems == ["gbv-command-centre: phone 'call me' has an unexpected format"]
