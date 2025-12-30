from record_verifier.config.sources import TRUSTED

def score(articles):
    score = 0
    for a in articles:
        for src, weight in TRUSTED.items():
            if src in a["source"].lower():
                score += weight
    return score