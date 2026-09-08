def infer_beam_region(log_text: str):
    """
    Very lightweight heuristic to infer likely beam/region
    based on known strings in the log.
    """
    text = log_text.lower()

    if "gulf of guinea" in text or "afr-ku" in text:
        return "AFRICA / GULF OF GUINEA REGION"

    if "north sea" in text or "eur-ku" in text:
        return "EUROPE / NORTH SEA REGION"

    if "pacific" in text or "pac-ku" in text:
        return "PACIFIC REGION"

    if "indian ocean" in text or "ind-ku" in text:
        return "INDIAN OCEAN REGION"

    return "UNKNOWN / GENERIC MARITIME REGION"
