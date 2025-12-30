from record_verifier.analysis.verdict import verdict

def test_verdict():
    assert verdict(0) == "No independent confirmation"
    assert verdict(2) == "Partial / unclear"
    assert verdict(6) == "Likely verified"