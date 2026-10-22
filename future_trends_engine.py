# ======================================================
# FUTURE TRENDS ENGINE v2.0
# AMC Academy Tech AI
# Phase 2 → Phase 6
# ======================================================

from datetime import datetime


class FutureTrendsEngine:
    def __init__(self, prompt=None):
        self.engine_name = "future_trends_engine"
        self.prompt = prompt or "future_trends_prompt.txt"

    # ======================================================
    # LOAD PROMPT
    # ======================================================
    def load_prompt(self):
        try:
            with open(f"prompts/{self.prompt}", "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return ""

    # ======================================================
    # BASE FORECAST OBJECT
    # ======================================================
    def _build_base_forecast(self, years, domain):
        return {
            "engine": self.engine_name,
            "timestamp": datetime.utcnow().isoformat(),
            "phase": f"Phase 6 - {years} Year Forecast",
            "domain": domain,
            "years_requested": years,
            "status": "Forecast generated successfully",
            "executive_summary": "",
            "technology_forecast": [],
            "market_forecast": [],
            "risk_forecast": [],
            "opportunities": [],
            "insights": [],
            "confidence": "Medium"
        }

    # ======================================================
    # SATCOM FORECAST
    # ======================================================
    def _satcom_forecast(self, forecast, years):

        forecast["executive_summary"] = (
            f"Over the next {years} years, SATCOM networks are expected "
            "to become increasingly AI-driven, software-defined, and LEO-enabled."
        )

        forecast["technology_forecast"] = [
            "Growth in LEO satellite constellations.",
            "Software-defined satellite networks.",
            "AI-assisted network optimisation.",
            "Dynamic beam allocation and routing."
        ]

        forecast["market_forecast"] = [
            "Increased maritime broadband adoption.",
            "Expansion of remote offshore connectivity.",
            "Greater demand for hybrid VSAT and terrestrial solutions."
        ]

        forecast["risk_forecast"] = [
            "Spectrum congestion.",
            "Cybersecurity threats.",
            "Orbital traffic coordination challenges."
        ]

        forecast["opportunities"] = [
            "Maritime connectivity services.",
            "Smart vessel platforms.",
            "SATCOM cybersecurity."
        ]

        forecast["insights"] = [
            f"Bandwidth demand may increase by approximately {years * 5}%.",
            "LEO latency improvements will transform operational communications."
        ]

        forecast["confidence"] = "High"

    # ======================================================
    # MARITIME FORECAST
    # ======================================================
    def _maritime_forecast(self, forecast, years):

        forecast["executive_summary"] = (
            f"Maritime operations are expected to undergo significant digital "
            f"transformation over the next {years} years."
        )

        forecast["technology_forecast"] = [
            "AI-assisted vessel operations.",
            "Digital twin technology.",
            "Predictive maintenance systems.",
            "Autonomous navigation support."
        ]

        forecast["market_forecast"] = [
            "Growth in smart ports.",
            "Expansion of digital logistics platforms.",
            "Integrated vessel intelligence solutions."
        ]

        forecast["risk_forecast"] = [
            "Cyber attacks on maritime infrastructure.",
            "Regulatory compliance complexity.",
            "Skills shortages."
        ]

        forecast["opportunities"] = [
            "Port intelligence platforms.",
            "Remote vessel diagnostics.",
            "Autonomous vessel support."
        ]

        forecast["insights"] = [
            f"Digitalisation adoption could exceed {40 + years}%.",
            "Hybrid VSAT + 5G offshore connectivity will become standard."
        ]

        forecast["confidence"] = "High"

    # ======================================================
    # CYBER FORECAST
    # ======================================================
    def _cyber_forecast(self, forecast, years):

        forecast["executive_summary"] = (
            "Cybersecurity will increasingly rely on AI and automation."
        )

        forecast["technology_forecast"] = [
            "AI-powered intrusion detection.",
            "Zero-trust architectures.",
            "Autonomous threat hunting."
        ]

        forecast["market_forecast"] = [
            "Increased compliance requirements.",
            "Higher cybersecurity investment."
        ]

        forecast["risk_forecast"] = [
            "Supply chain attacks.",
            "AI-generated threats.",
            "Critical infrastructure targeting."
        ]

        forecast["opportunities"] = [
            "Managed security services.",
            "Maritime cyber intelligence.",
            "Compliance automation."
        ]

        forecast["insights"] = [
            "Signature-based security will gradually be replaced by AI-driven systems.",
            f"Cyber maturity could improve by approximately {years * 10}%."
        ]

        forecast["confidence"] = "High"

    # ======================================================
    # AI AUTOMATION FORECAST
    # ======================================================
    def _ai_forecast(self, forecast, years):

        forecast["executive_summary"] = (
            "AI copilots will become integrated into daily operations."
        )

        forecast["technology_forecast"] = [
            "Operational AI copilots.",
            "Autonomous workflow systems.",
            "Decision-support engines."
        ]

        forecast["market_forecast"] = [
            "Wide-scale AI deployment.",
            "Growth of autonomous support systems."
        ]

        forecast["risk_forecast"] = [
            "Model governance challenges.",
            "AI misuse risks."
        ]

        forecast["opportunities"] = [
            "AI-assisted compliance.",
            "Predictive analytics.",
            "Intelligent automation."
        ]

        forecast["insights"] = [
            f"Automation penetration could reach {20 + years}%.",
            "AI copilots may become standard business tools."
        ]

        forecast["confidence"] = "High"

    # ======================================================
    # GHANA MARITIME SPECIALIST LOGIC
    # ======================================================
    def _apply_ghana_logic(self, forecast):

        forecast["technology_forecast"].extend([
            "Expansion of LEO maritime services in the Gulf of Guinea.",
            "AI-powered logistics at Tema Port.",
            "Digital transformation initiatives at Takoradi Port."
        ])

        forecast["market_forecast"].extend([
            "Growth in offshore energy connectivity.",
            "Increased demand for vessel tracking.",
            "Expansion of maritime cybersecurity services."
        ])

        forecast["insights"].extend([
            "Ghana could become a West African maritime intelligence hub.",
            "Port automation and vessel visibility are expected to increase."
        ])

        forecast["confidence"] = "High"

    # ======================================================
    # MAIN FORECAST GENERATOR
    # ======================================================
    def generate_forecast(self, years, domain):

        domain_lower = str(domain).lower()

        forecast = self._build_base_forecast(years, domain)

        if "satcom" in domain_lower:
            self._satcom_forecast(forecast, years)

        elif "maritime" in domain_lower:
            self._maritime_forecast(forecast, years)

        elif "cyber" in domain_lower:
            self._cyber_forecast(forecast, years)

        elif "ai" in domain_lower:
            self._ai_forecast(forecast, years)

        else:
            forecast["insights"].append(
                "Domain recognised but no specialist model available."
            )

        if "ghana" in domain_lower:
            self._apply_ghana_logic(forecast)

        if years >= 20:
            forecast["insights"].extend([
                "Semi-autonomous merchant vessels likely.",
                "AI-managed fleet operations expected.",
                "Port digital twin ecosystems may become standard.",
                "Predictive maritime maintenance platforms could dominate.",
                "Integrated SATCOM-AI infrastructures likely."
            ])

        return {
            "analysis": forecast["executive_summary"],
            "summary": f"{years}-year forecast generated for {domain}.",
            "forecast": forecast,
            "confidence": forecast["confidence"]
        }

    # ======================================================
    # PUBLIC ENTRY POINT
    # ======================================================
    def predict_any(self, years, domain="maritime"):

        if years == "enterprise":
            years = 25

        try:
            years = int(years)
        except Exception:
            years = 5

        return self.generate_forecast(years, domain)

