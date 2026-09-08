"""
SATCOM Insights Engine Wrapper
AMC Academy Tech AI — SATCOM Reasoning Engine v3

This file acts as the clean interface between the main
satcom_reasoning_service.py engine and the modular insights
located in /satcom_insights/.
"""

from satcom_insights.insight_bundle import build_satcom_insight_bundle


def run_satcom_insights(log_text: str):
    """
    Wrapper for SATCOM Insights:
    - Alarm clustering
    - Severity scoring
    - Beam region inference

    Returns None if no log text is provided.
    """
    if not log_text:
        return None

    try:
        return build_satcom_insight_bundle(log_text)
    except Exception as e:
        # Fail-safe: never break the main engine
        return {
            "error": "satcom_insights_engine_failed",
            "details": str(e)
        }
