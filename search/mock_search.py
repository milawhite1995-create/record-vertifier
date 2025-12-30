def search(name, location):
    """
    Mock search results.
    Replace later with real APIs.
    """
    MOCK_DB = {
        "Kristoffer McAlpine": [
            {"source": "The Courier", "text": "Glenrothes man convicted of abusive behaviour"}
        ]
    }
    return MOCK_DB.get(name, [])