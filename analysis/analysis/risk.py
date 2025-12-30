def flags(name, articles):
    f = []
    if len(name.split()) <= 2:
        f.append("Common name")
    if not articles:
        f.append("No independent sources")
    return f