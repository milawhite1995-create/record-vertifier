def search(name, location):
    """
    NewsAPI / GNews search results.
    NewsAPI / GNews
    """
    MOCK_DB = {
        "Kristoffer McAlpine": [
            {"source": "The Courier", "text": "Glenrothes man convicted of abusive behaviour"}
        ]
    }
    return MOCK_DB.get(name, [])