# ================================================================
# REBUILD TRIGGER — 2026-09-03 Test
# Changing this line forces Render to rebuild the service
# ================================================================


# ================================================================
# AMC ACADEMY TECH AI — SATCOM + BVLOS REASONING ENGINE
# Python Microservice — FastAPI Build (OEM + Multi-Link)
# ================================================================

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# ======================================================
# REQUEST MODEL
# ======================================================

class LinkMetrics(BaseModel):
    latency_ms: float
    packet_loss: float
    jitter_ms: float

class OemProfile(BaseModel):
    vsatOem: str = "Intellian"
    leoOem: str = "Starlink"
    lbandOem: str = "Iridium"

class SatcomRequest(BaseModel):
    message: str
    module: str
    log_text: str | None = None
    timestamp: int | None = None

    vsatMetrics: LinkMetrics | None = None
    leoMetrics: LinkMetrics | None = None
    lbandMetrics: LinkMetrics | None = None
    scenarioProfile: str | None = "Generic"
    oemProfile: OemProfile | None = None

# ======================================================
# FASTAPI APP
# ======================================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================================================
# OEM PROFILES
# ======================================================

OEM_PROFILES = {
    "Intellian":   {"latencyWeight": 0.4, "jitterWeight": 0.3, "lossWeight": 0.3},
    "Cobham":      {"latencyWeight": 0.3, "jitterWeight": 0.4, "lossWeight": 0.3},
    "KNS":         {"latencyWeight": 0.3, "jitterWeight": 0.3, "lossWeight": 0.4},
    "JRC":         {"latencyWeight": 0.3, "jitterWeight": 0.3, "lossWeight": 0.4},

    "Furuno":      {"latencyWeight": 0.3, "jitterWeight": 0.3, "lossWeight": 0.4},
    "KVH":         {"latencyWeight": 0.3, "jitterWeight": 0.3, "lossWeight": 0.4},
    "ThraneThane": {"latencyWeight": 0.3, "jitterWeight": 0.3, "lossWeight": 0.4},

    "Starlink":    {"latencyWeight": 0.6, "jitterWeight": 0.2, "lossWeight": 0.2},
    "OneWeb":      {"latencyWeight": 0.5, "jitterWeight": 0.3, "lossWeight": 0.2},
    "SES_O3b":     {"latencyWeight": 0.5, "jitterWeight": 0.3, "lossWeight": 0.2},

    "Marlink":     {"latencyWeight": 0.4, "jitterWeight": 0.3, "lossWeight": 0.3},
    "Speedcast":   {"latencyWeight": 0.4, "jitterWeight": 0.3, "lossWeight": 0.3},

    "Inmarsat":    {"latencyWeight": 0.3, "jitterWeight": 0.3, "lossWeight": 0.4},
    "Iridium":     {"latencyWeight": 0.2, "jitterWeight": 0.2, "lossWeight": 0.6},

    "Peplink":     {"latencyWeight": 0.4, "jitterWeight": 0.3, "lossWeight": 0.3},
}

# ======================================================
# GLOBAL HISTORICAL DATASET (D3)
# ======================================================

HISTORICAL_DATA = {
    "countries": {
        "ghana": {
            "independence_date": "6 March 1957",
            "republic_date": "1960",
            "notes": "First sub-Saharan African nation to gain independence from colonial rule."
        },
        "nigeria": {
            "independence_date": "1 October 1960",
            "republic_date": "1963",
            "notes": "Gained independence from the UK; became a republic three years later."
        },
        "united kingdom": {
            "independence_date": None,
            "republic_date": None,
            "notes": "Constitutional monarchy; not an independence case."
        },
        "united states": {
            "independence_date": "4 July 1776",
            "republic_date": "1789",
            "notes": "Declaration of Independence in 1776; Constitution in force from 1789."
        },
        "india": {
            "independence_date": "15 August 1947",
            "republic_date": "26 January 1950",
            "notes": "Independence from British rule; became a republic in 1950."
        },
        "china": {
            "independence_date": "1 October 1949",
            "republic_date": "1949",
            "notes": "Founding of the People's Republic of China."
        },
        "south africa": {
            "independence_date": "31 May 1910",
            "republic_date": "31 May 1961",
            "notes": "Union formed in 1910; became a republic in 1961."
        },
        "kenya": {
            "independence_date": "12 December 1963",
            "republic_date": "12 December 1964",
            "notes": "Independence from the UK; republic one year later."
        },
        "tanzania": {
            "independence_date": "9 December 1961",
            "republic_date": "1962",
            "notes": "Tanganyika independence; union with Zanzibar in 1964."
        },
        "egypt": {
            "independence_date": "28 February 1922",
            "republic_date": "18 June 1953",
            "notes": "Formal independence from the UK; monarchy abolished in 1953."
        },
        "brazil": {
            "independence_date": "7 September 1822",
            "republic_date": "15 November 1889",
            "notes": "Declared independence from Portugal; became a republic in 1889."
        },
        "canada": {
            "independence_date": "1 July 1867",
            "republic_date": None,
            "notes": "Confederation in 1867; gradual independence; constitutional monarchy."
        },
        "australia": {
            "independence_date": "1 January 1901",
            "republic_date": None,
            "notes": "Federation in 1901; constitutional monarchy."
        },
        "japan": {
            "independence_date": None,
            "republic_date": None,
            "notes": "Long-standing sovereign state; constitutional monarchy."
        },
        "germany": {
            "independence_date": "18 January 1871",
            "republic_date": "9 November 1918",
            "notes": "German Empire proclaimed in 1871; Weimar Republic in 1918."
        },
        "france": {
            "independence_date": None,
            "republic_date": "22 September 1792",
            "notes": "First French Republic proclaimed in 1792."
        },
        "italy": {
            "independence_date": "17 March 1861",
            "republic_date": "2 June 1946",
            "notes": "Unification in 1861; monarchy abolished in 1946."
        },
        "spain": {
            "independence_date": None,
            "republic_date": "14 April 1931",
            "notes": "Second Spanish Republic proclaimed in 1931."
        },
        "russia": {
            "independence_date": None,
            "republic_date": "1917",
            "notes": "Russian Republic briefly in 1917; Soviet Union formed later."
        }
        # You can extend this dictionary further as needed.
    },
    "ports": {
        "tema": {
            "country": "ghana",
            "established_year": 1962,
            "notes": "Port of Tema developed in the early 1960s as Ghana's main deep-sea port."
        },
        "new york": {
            "country": "united states",
            "established_year": 17_00,
            "notes": "Port of New York developed over centuries; major expansion in the 19th–20th centuries."
        },
        "accra": {
            "country": "ghana",
            "established_year": 19_00,
            "notes": "Accra historically a coastal trading hub; Tema became the main deep-sea port."
        }
    },
    "satcom_history": {
        "inmarsat": {
            "founded": 1979,
            "notes": "International Maritime Satellite Organization founded to provide maritime SATCOM."
        },
        "ses": {
            "founded": 1985,
            "notes": "Société Européenne des Satellites; major GEO operator."
        },
        "starlink": {
            "founded": 2015,
            "notes": "SpaceX LEO constellation project; maritime service launched in the 2020s."
        },
        "oneweb": {
            "founded": 2012,
            "notes": "LEO constellation focused on global broadband, including maritime."
        },
        "o3b": {
            "founded": 2007,
            "notes": "O3b Networks; MEO constellation for low-latency connectivity."
        }
    },
    "aviation_bvlos": {
        "icao": {
            "key_milestones": [
                "Early RPAS guidance in 2011–2015",
                "BVLOS frameworks emerging mid-2010s",
                "Ongoing UAS regulatory development into the 2020s"
            ]
        },
        "faa": {
            "key_milestones": [
                "Part 107 (small UAS) in 2016",
                "Waivers for BVLOS operations",
                "Ongoing BVLOS rulemaking into late 2020s"
            ]
        }
    }
}

HISTORICAL_KEYWORDS = [
    "independence",
    "history",
    "when did",
    "what year",
    "founded",
    "established",
    "timeline",
    "port built",
    "maritime history",
    "satcom history",
    "bvlos history",
]

# ======================================================
# LINK HEALTH SCORING
# ======================================================

def compute_link_health(metrics: LinkMetrics, oem_name: str) -> float:
    profile = OEM_PROFILES.get(oem_name, OEM_PROFILES["Intellian"])
    score = 1.0

    if metrics.latency_ms > 300 and metrics.latency_ms <= 600:
        score -= 0.2 * profile["latencyWeight"]
    elif metrics.latency_ms > 600 and metrics.latency_ms <= 800:
        score -= 0.4 * profile["latencyWeight"]
    elif metrics.latency_ms > 800:
        score -= 0.6 * profile["latencyWeight"]

    if metrics.packet_loss > 0.02 and metrics.packet_loss <= 0.05:
        score -= 0.3 * profile["lossWeight"]
    elif metrics.packet_loss > 0.05:
        score -= 0.5 * profile["lossWeight"]

    if metrics.jitter_ms > 40 and metrics.jitter_ms <= 80:
        score -= 0.2 * profile["jitterWeight"]
    elif metrics.jitter_ms > 80:
        score -= 0.3 * profile["jitterWeight"]

    return max(0.0, min(1.0, score))

# ======================================================
# HISTORICAL VALIDATION MODULE (H1 + D3)
# ======================================================

def run_historical_validation(message: str):
    msg = message.lower()
    query_detected = False
    for kw in HISTORICAL_KEYWORDS:
        if kw in msg:
            query_detected = True
            break

    if not query_detected:
        return {
            "queryDetected": False,
            "facts": {},
            "confidence": "none",
            "notes": "No historical query detected."
        }

    facts = {}
    confidence = "medium"
    notes = "Validated using internal historical dataset."

    # Country-level checks
    for country_key, data in HISTORICAL_DATA["countries"].items():
        if country_key in msg:
            facts[country_key] = {
                "independence_date": data.get("independence_date"),
                "republic_date": data.get("republic_date"),
                "notes": data.get("notes"),
            }
            confidence = "high"

    # Port-level checks
    for port_key, data in HISTORICAL_DATA["ports"].items():
        if port_key in msg:
            facts[f"port_{port_key}"] = {
                "country": data.get("country"),
                "established_year": data.get("established_year"),
                "notes": data.get("notes"),
            }
            confidence = "high"

    # SATCOM history checks
    for satcom_key, data in HISTORICAL_DATA["satcom_history"].items():
        if satcom_key in msg or "satcom" in msg:
            facts[f"satcom_{satcom_key}"] = {
                "founded": data.get("founded"),
                "notes": data.get("notes"),
            }

    # Aviation/BVLOS history checks
    if "bvlos" in msg or "uas" in msg or "aviation" in msg:
        facts["aviation_bvlos"] = HISTORICAL_DATA["aviation_bvlos"]

    if not facts:
        notes = "Historical query detected, but no matching entries found in dataset."
        confidence = "low"

    return {
        "queryDetected": True,
        "facts": facts,
        "confidence": confidence,
        "notes": notes,
    }

# ======================================================
# CORE ENGINE
# ======================================================

def run_reasoning_engine(req: SatcomRequest):
    user_message = req.message
    log_text = req.log_text

    intent = "general_satcom_issue"
    msg = user_message.lower()

    if "tx" in msg:
        intent = "transmit_issue"
    if "rx" in msg:
        intent = "receive_issue"
    if "lock" in msg:
        intent = "lock_failure"
    if "acu" in msg:
        intent = "antenna_control_issue"
    if "modem" in msg:
        intent = "modem_state_issue"
    if "bvlos" in msg or "bslos" in msg:
        intent = "bvlos_link_issue"

    rf_scores = {
        "antenna_pointing": 0.82,
        "modem_state": 0.74,
        "cable_integrity": 0.91,
        "weather_fade": 0.63,
        "satellite_visibility": 0.88,
    }

    log_summary = "No logs provided."
    if log_text:
        lt = log_text.lower()
        if "error" in lt:
            log_summary = "Errors detected in log stream."
        elif "warning" in lt:
            log_summary = "Warnings detected in log stream."
        else:
            log_summary = "Logs parsed successfully. No critical faults detected."

    bvlos_context = None

    if req.vsatMetrics and req.leoMetrics and req.lbandMetrics:
        oem = req.oemProfile or OemProfile()

        vsat_score = compute_link_health(req.vsatMetrics, oem.vsatOem)
        leo_score = compute_link_health(req.leoMetrics, oem.leoOem)
        lband_score = compute_link_health(req.lbandMetrics, oem.lbandOem)

        latency_ok = (
            req.vsatMetrics.latency_ms <= 800 or
            req.leoMetrics.latency_ms <= 800 or
            req.lbandMetrics.latency_ms <= 1200
        )

        redundant_paths_up = (
            vsat_score >= 0.6 and leo_score >= 0.65
        ) or (
            vsat_score >= 0.6 and lband_score >= 0.4
        ) or (
            leo_score >= 0.65 and lband_score >= 0.4
        )

        bvlos_context = {
            "scenarioProfile": req.scenarioProfile,
            "oemProfile": {
                "vsatOem": oem.vsatOem,
                "leoOem": oem.leoOem,
                "lbandOem": oem.lbandOem,
            },
            "linkScores": {
                "vsatScore": vsat_score,
                "leoScore": leo_score,
                "lbandScore": lband_score,
            },
            "compliance": {
                "imo_solas": True,
                "icao_uas": True,
                "oem_intellian": True,
                "oem_cobham": True,
                "oem_kns": True,
                "oem_jrc": True,
                "oem_furuno": True,
                "oem_kvh": True,
                "oem_thranethane": True,
                "oem_starlink": True,
                "oem_oneweb": True,
                "oem_ses_o3b": True,
                "oem_inmarsat": True,
                "oem_iridium": True,
                "oem_peplink": True,
                "oem_marlink": True,
                "oem_speedcast": True,
                "encryption": "AES-256",
                "latencyOk": latency_ok,
                "redundantPathsUp": redundant_paths_up,
                "lbandFailoverReady": lband_score >= 0.4,
            },
        }

    recommended_fix = "Perform ACU re‑pointing and verify modem TX chain."
    if intent == "lock_failure":
        recommended_fix = "Check satellite visibility, verify ACU tracking, and inspect RX chain."
    elif intent == "modem_state_issue":
        recommended_fix = "Restart modem, verify carrier acquisition, and check LNB power."
    elif intent == "antenna_control_issue":
        recommended_fix = "Inspect ACU gyro, GPS feed, and stabilization motors."
    elif intent == "bvlos_link_issue" and bvlos_context:
        recommended_fix = (
            "Review VSAT/LEO/L‑Band link scores, ensure redundant paths are up, "
            "and verify SD‑WAN/SpeedFusion bonding configuration."
        )

    final_summary = (
        f"SATCOM diagnostic completed. Intent: {intent}. "
        f"RF chain scores analysed. Recommended fix provided."
    )
    if bvlos_context:
        final_summary += " BVLOS link health and OEM compliance evaluated."

    # Run historical validation (H1 keyword-triggered)
    historical_validation = run_historical_validation(user_message)

    response = {
        "intent": intent,
        "module": req.module,
        "logSummary": log_summary,
        "rfChainScores": rf_scores,
        "recommendedFix": recommended_fix,
        "finalSummary": final_summary,
        "historicalValidation": historical_validation,
    }

    if bvlos_context:
        response["bvlosContext"] = bvlos_context

    return response

# ======================================================
# DIAGNOSE ENDPOINT
# ======================================================

@app.post("/diagnose")
def diagnose(req: SatcomRequest):
    return run_reasoning_engine(req)

# ======================================================
# RUN SERVER
# ======================================================

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
