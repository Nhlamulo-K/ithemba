from directory_api.filtering import filter_by_province

entries = [
    {
        "id": "helpline",
        "name": "Helpline",
        "type": "helpline",
        "province": "national",
        "phone": "0800 428 428",
        "source_url": "https://sanews.gov.za/node/61236",
        "last_verified": "2026-09-24",
    },
    {
        "id": "gauteng-tcc",
        "name": "Gauteng TCC",
        "type": "thuthuzela",
        "province": "gauteng",
        "phone": "0800 428 428",
        "source_url": "https://sanews.gov.za/node/61236",
        "last_verified": "2026-09-24",
    },
    {
        "id": "cape-clinic",
        "name": "Cape Clinic",
        "type": "clinic",
        "province": "western-cape",
        "phone": "0800 428 428",
        "source_url": "https://sanews.gov.za/node/61236",
        "last_verified": "2026-09-24",
    }
]

def test_Province_filter_includes_national_entries():
    entry = entries
    problems = filter_by_province(entry, "gauteng")
    assert [entry["id"] for entry in problems] == ["helpline", "gauteng-tcc"]

def test_province_with_no_entries_still_gets_national():
    entry = entries
    problems = filter_by_province(entry, "limpopo")
    assert [entry["id"] for entry in problems] == ["helpline"]