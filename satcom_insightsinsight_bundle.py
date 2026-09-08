from .clustering import cluster_alarms
from .severity import score_alarm_severity
from .beam_region import infer_beam_region


def build_satcom_insight_bundle(log_text: str):
    """
    Compose a single insight bundle from:
    - alarm clustering
    - severity scoring
    - beam region hint
    """
    clusters = cluster_alarms(log_text)
    severity = score_alarm_severity(log_text)
    region_hint = infer_beam_region(log_text)

    return {
        "alarmClusters": clusters,
        "severity": severity,
        "beamRegionHint": region_hint,
    }
