import math as m

def get_orbital_period(grav_param: float, semimajoraxis: float) -> float:
    period = 2 * m.pi * m.sqrt(semimajoraxis**3/grav_param)
    return period

