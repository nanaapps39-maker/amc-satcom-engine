from .vessel_profiles import VESSEL_TYPES


def get_vessel_profile(vessel_type):

    return VESSEL_TYPES.get(
        vessel_type.lower(),
        {
            "service_speed": 14,
            "fuel_burn_tpd": 40
        }
    )


def calculate_eta(distance_nm, speed_knots):

    if speed_knots <= 0:
        return None

    hours = distance_nm / speed_knots

    return {
        "hours": round(hours, 2),
        "days": round(hours / 24, 2)
    }


def calculate_fuel_consumption(
    vessel_type,
    voyage_days
):

    profile = get_vessel_profile(vessel_type)

    fuel = profile["fuel_burn_tpd"] * voyage_days

    return round(fuel, 2)

def generate_voyage_analysis(
    vessel_type,
    distance_nm
):

    profile = get_vessel_profile(vessel_type)

    eta = calculate_eta(
        distance_nm,
        profile["service_speed"]
    )

    fuel = calculate_fuel_consumption(
        vessel_type,
        eta["days"]
    )

    return {
        "vessel_type": vessel_type,
        "distance_nm": distance_nm,
        "service_speed": profile["service_speed"],
        "eta_hours": eta["hours"],
        "eta_days": eta["days"],
        "fuel_consumption_tonnes": fuel
    }