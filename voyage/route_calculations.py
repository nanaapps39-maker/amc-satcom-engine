from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2


def calculate_great_circle_distance(
    lat1,
    lon1,
    lat2,
    lon2
):

    R = 3440.065

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return round(R * c, 2)

def calculate_voyage_time(
    distance_nm,
    speed_knots
):

    if speed_knots <= 0:
        return None

    hours = distance_nm / speed_knots

    return {
        "hours": round(hours, 2),
        "days": round(hours / 24, 2)
    }


def calculate_route_efficiency(
    great_circle_distance,
    actual_route_distance
):

    if actual_route_distance <= 0:
        return None

    efficiency = (
        great_circle_distance /
        actual_route_distance
    ) * 100

    return round(efficiency, 2)
