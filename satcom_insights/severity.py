SEVERITY_MAP = {
    # Example mappings – extend with your real alarm codes
    "ALM-102": 3,  # TX MUTE ACTIVE
    "ALM-305": 2,  # MODEM IF INPUT LOW
    "ALM-501": 3,  # TRACKING LOST
    "ALM-011": 1,  # GPS SIGNAL DEGRADED
    "ALM-402": 2,  # GYRO DATA INVALID
}


def score_alarm_severity(log_text: str):
    """
    Assign severity scores to alarms found in the log.
    Returns overall severity and per-alarm entries.
    """
    lines = log_text.splitlines()
    scored = []

    for line in lines:
        for code, severity in SEVERITY_MAP.items():
            if code in line:
                scored.append(
                    {
                        "code": code,
                        "severity": severity,
                        "raw": line.strip(),
                    }
                )

    if not scored:
        overall_severity_value = 0
    else:
        overall_severity_value = max(item["severity"] for item in scored)

    level_map = {
        0: "none",
        1: "low",
        2: "medium",
        3: "high",
    }
    overall_level = level_map.get(overall_severity_value, "none")

    return {
        "overallSeverity": overall_level,
        "overallSeverityValue": overall_severity_value,
        "alarms": scored,
    }
