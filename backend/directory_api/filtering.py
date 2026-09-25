def filter_by_province(entries, province):
    result =[]
    for entry in entries:
        if entry["province"] == province or entry["province"] == "national":
            result.append(entry)
    return result

def filter_by_type(entries, type):
    result = []
    for entry in entries:
        if entry["type"] == type:
            result.append(entry)
    return result