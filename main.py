import time as t
import matplotlib.pyplot as plt

import fns
import vals


if __name__ == "__main__":
    print("Starting calculations")
    starttime = t.time_ns()
    # call the functions here

    orbitalperiod = fns.get_orbital_period(vals.mercury_grav_parameter, vals.final_sma)
    orbitalfrequency = 1/orbitalperiod
    rot_degrees_p_sec = 360 * orbitalfrequency
    print("orbital period =", orbitalperiod, "s")
    print("rotational speed in deg/s =", rot_degrees_p_sec)

    solarpanel_maxtorque = fns.solarpaneltorque(vals.solarpanel_mass, vals.solarpanel_width, vals.solarpanel_time_for_180_rotation)
    print("solar panel rotation disturbance torque =", solarpanel_maxtorque, "Nm")

    if vals.Config.x_m > (vals.Torques.dist * (1+vals.margin_factor)):
        print("x thrusters sufficient for dist. torque")
    if vals.Config.y_m > (vals.Torques.dist * (1+vals.margin_factor)):
        print("y thrusters sufficient for dist. torque")
    if vals.Config.z_m > (vals.Torques.dist * (1+vals.margin_factor)):
        print("z thrusters sufficient for dist. torque")
    if vals.Config.RW_torque > (vals.Torques.dist * (1+vals.margin_factor)):
        print("reaction wheels sufficient for dist. torque")
    
    if vals.Config.x_m > vals.Manoevre_torqs.torque_x:
        print("x thrusters sufficient for manouvre")
    if vals.Config.y_m > vals.Manoevre_torqs.torque_x:
        print("y thrusters sufficient for manouvre")
    if vals.Config.z_m > vals.Manoevre_torqs.torque_x:
        print("z thrusters sufficient for manouvre")
    if vals.Config.RW_torque > vals.Manoevre_torqs.maxtorque:
        print("reaction wheels sufficient for manouvre")



    print("Calculations finished")
    time_taken = round((t.time_ns() - starttime)/1e9, 3)
    print("Took", time_taken, "seconds")

    vals.Torques


