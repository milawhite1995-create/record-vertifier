def search(name, location):
    """
    Mock search results.
    NewsAPI / GNews
    """
    MOCK_DB = {
        "Kristoffer McAlpine": [
            {"source": "The Courier", "text": "Glenrothes man convicted of abusive behaviour"}
        ]
    }
    return MOCK_DB.get(name, [])