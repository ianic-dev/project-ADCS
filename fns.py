import math as m

def get_orbital_period(grav_param: float, semimajoraxis: float) -> float:
    period = 2 * m.pi * m.sqrt(semimajoraxis**3/grav_param)
    return period

def panel_moment_inertia(mass: float, width: float)  -> float:
    I = 1/12
    I *= mass
    I *= width**2
    return I

def solarpaneltorque(mass: float, width: float, time: float) -> float:
    inertia = panel_moment_inertia(mass, width)
    acceleration = m.pi/(time**2)
#    print("solar panel acceleration =", acceleration)
#    print("solar panel inertia =", inertia)
    torque = acceleration*inertia
    return torque
