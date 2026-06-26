def normalize_indicator(indicator, source, indicator_type="URL"):

    risk_scores = {
        "OpenPhish": 90,
        "URLhaus": 95,
        "AlienVault": 85
    }

    return {
        "indicator": indicator,
        "type": indicator_type,
        "source": source,
        "risk_score": risk_scores.get(source, 50)
    }