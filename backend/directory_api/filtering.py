def filter_by_province(entries, province):
    result =[]
    for entry in entries:
        if entry["province"] == province or entry["province"] == "national":
            result.append(entry)
    return result