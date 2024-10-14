import math as m

def get_orbital_period(grav_param: float, semimajoraxis: float) -> float:
    period = 2 * m.pi * m.sqrt(semimajoraxis**3/grav_param)
    return period

def panel_moment_inertia(mass: float, width: float)  -> float:
    I = 1/12
    I *= mass
    I *= width**2
    return I

def max_moment_inertia(panel_length: float, panel_width: float, panel_mass: float, body_mass: float, boom_length: float) -> float:
    I_panel = (1/12) * panel_mass * (panel_width*panel_length)
    I_body = body_mass*1.6**4/12
    I_magnet = 2 * (boom_length+0.8)**2 * 0.2
    return I_panel + I_body + I_magnet


def solarpaneltorque(mass: float, width: float, time: float) -> float:
    inertia = panel_moment_inertia(mass, width)
    acceleration = m.pi/(time**2)
#    print("solar panel acceleration =", acceleration)
#    print("solar panel inertia =", inertia)
    torque = acceleration*inertia
    return torque

def mininertia(panel_mass: float, panel_width: float, body_mass: float, boomlen: float) -> float:
    Ipanel = panel_moment_inertia(panel_mass, panel_width)
    Ibody = body_mass*1.6**4/12
    Imagnet = 2 * (boomlen+0.8)**2 * 0.2
    return Ipanel + Ibody + Imagnet

def maxgravtorque(gravparam: float, sma: float, Imax: float, Imin: float) -> float:
    n = m.sqrt(gravparam/(sma**3))
    torque = n**2 * 3/2
    torque *= (Imax-Imin)
    return torque


