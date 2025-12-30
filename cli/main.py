from record_verifier.ingestion.load_entries import load_entries
from record_verifier.search.mock_search import search
from record_verifier.analysis.credibility import score
from record_verifier.analysis.verdict import verdict
from record_verifier.analysis.risk import flags
from record_verifier.reporting.export import export

def run():
    entries = load_entries("data/raw/entries.csv")
    results = []

    for e in entries:
        articles = search(e["name"], e["location"])
        s = score(articles)
        results.append({
            **e,
            "score": s,
            "verdict": verdict(s),
            "risk_flags": "; ".join(flags(e["name"], articles))
        })

    export(results, "data/processed/results.csv")
    print("✔ Verification complete")