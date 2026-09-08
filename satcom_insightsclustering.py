from collections import defaultdict
from datetime import datetime


def parse_alarm_line(line: str):
    """
    Parse a single alarm line.

    Expected format example:
    [2026-07-25 18:03:11] ALM-102: TX MUTE ACTIVE
    """
    try:
        if "ALM-" not in line:
            return None

        ts_part, rest = line.split("]", 1)
        ts_str = ts_part.strip().lstrip("[")
        code_part, desc_part = rest.split(":", 1)

        code = code_part.strip()
        desc = desc_part.strip()

        ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")

        return {
            "timestamp": ts,
            "code": code,
            "description": desc,
            "raw": line.strip(),
        }
    except Exception:
        return None


def cluster_alarms(log_text: str):
    """
    Group alarms by code and compute basic stats per cluster.
    """
    lines = log_text.splitlines()
    alarms = []

    for line in lines:
        parsed = parse_alarm_line(line)
        if parsed:
            alarms.append(parsed)

    clusters = defaultdict(list)
    for alarm in alarms:
        clusters[alarm["code"]].append(alarm)

    summary = []
    for code, events in clusters.items():
        events_sorted = sorted(events, key=lambda x: x["timestamp"])
        first_ts = events_sorted[0]["timestamp"]
        last_ts = events_sorted[-1]["timestamp"]
        duration_minutes = (last_ts - first_ts).total_seconds() / 60.0

        summary.append(
            {
                "code": code,
                "count": len(events_sorted),
                "firstTimestamp": first_ts.isoformat(),
                "lastTimestamp": last_ts.isoformat(),
                "durationMinutes": round(duration_minutes, 2),
            }
        )

    return {
        "clusterCount": len(summary),
        "clusters": summary,
    }
