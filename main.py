import time as t
import matplotlib.pyplot as plt
import numpy as np

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

    dist_req = (vals.Torques.dist * (1+vals.margin_factor))

    #'''
    fig, ax = plt.subplots()
    axes = ("x", "y", "z")
    x = np.arange(len(axes))
    data = {
        'Disturbance torque (with margin factor)': (dist_req, dist_req, dist_req),
        'Manoevre torque': (vals.Manoevre_torqs.torque_x, vals.Manoevre_torqs.torque_y, vals.Manoevre_torqs.torque_z),
    }

    width = 0.3333

    bar_n = 0
    for requirement, value in data.items():
        print("isgood")
        offset = width*bar_n
        rects = ax.bar(x+offset,value,width,label=requirement)
        ax.bar_label(rects, padding=2)
        bar_n += 1
    ax.set_ylabel("Torque requirement [Nm]")
    ax.set_xticks(x+width, axes)
    ax.set_yscale('log')
    ax.legend(loc='upper left', ncols=3)
    #'''

    '''

    fig, ax = plt.subplots()
    axes = ("x", "y", "z")
    x = np.arange(len(axes))
    data = {
        'Thruster torque': (vals.Config.x_m, vals.Config.y_m, vals.Config.z_m),
        'Reaction wheel torque': (vals.Config.RW_torque, vals.Config.RW_torque, vals.Config.RW_torque),
        'Torque requirement': (vals.Manoevre_torqs.torque_x, vals.Manoevre_torqs.torque_y, vals.Manoevre_torqs.torque_z),
    }

    width = 0.25

    bar_n = 0
    for source, value in data.items():
        offset = width*bar_n
        rects = ax.bar(x+offset,value,width,label=source)
        ax.bar_label(rects, padding=3)
        bar_n+=1
    ax.set_ylabel("Torque [Nm]")
    ax.set_xticks(x+width, axes)
    ax.set_yscale('linear')
    ax.set_ylim(0, 2)
    ax.legend(loc='upper left', ncols=3)

    #'''

    



    print("Calculations finished")
    time_taken = round((t.time_ns() - starttime)/1e9, 3)
    print("Took", time_taken, "seconds")
    plt.show()

    vals.Torques


