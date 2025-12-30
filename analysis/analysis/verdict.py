from record_verifier.config.settings import MIN_VERIFIED, PARTIAL

def verdict(score):
    if score >= MIN_VERIFIED:
        return "Likely verified"
    if score >= PARTIAL:
        return "Partial / unclear"
    return "No independent confirmation"