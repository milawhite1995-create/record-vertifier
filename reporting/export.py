import pandas as pd

def export(results, path):
    pd.DataFrame(results).to_csv(path, index=False)