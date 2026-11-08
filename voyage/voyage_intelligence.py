from .vessel_profiles import VESSEL_TYPES


def get_vessel_profile(vessel_type):

    return VESSEL_TYPES.get(
        vessel_type.lower(),
        {
            "service_speed": 14,
            "fuel_burn_tpd": 40
        }
    )