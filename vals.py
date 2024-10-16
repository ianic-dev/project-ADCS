import math as m

mercury_radius = 2439.7e3
mercury_grav_parameter = 2.20329e13

eclipes_fraction = 0.277

final_sma = mercury_radius + 750e3
max_disturbance_torque = "idk"

solarpanel_time_for_180_rotation_mins = 35.23
solarpanel_time_for_180_rotation = solarpanel_time_for_180_rotation_mins*60

solarpanel_area = 25.45
solarpanel_width = 1.4
solarpanel_mass = 10.18
solarpanel_length = 1.6 + solarpanel_area/solarpanel_width

magnetboom_length = 10.5



margin_factor = 0.4

"""------ WP3 ---------"""


class MoI:
    x = 854.92
    y = 830.18
    z = 716.473


class Torques:
    spanel = 1.169e-6
    grav_grad = ((mercury_grav_parameter/(final_sma**3))*3/2) * (max(MoI.x, MoI.y, MoI.z) - min(MoI.x, MoI.y, MoI.z))
    magnetic = 2e-8
    dist = spanel+grav_grad+magnetic
    print("torque = ", dist)


class Config:
    x_arm = 0.9
    x_npairs = 2
    thrust = 1
    min_impulse = 0.043
    y_arm = 0.9
    y_npairs = 1
    z_arm = 0.9
    z_npairs = 2

    x_m = x_arm*x_npairs*thrust
    y_m = y_arm*y_npairs*thrust
    z_m = z_arm*z_npairs*thrust

    

    RW_torque = 1

class Manoevre_torqs:
    time = 180
    angle = m.radians(90)
    torque_x = 4*MoI.x*angle/(time**2)
    torque_y = 4*MoI.y*angle/(time**2)
    torque_z = 4*MoI.z*angle/(time**2)
    maxtorque = max(torque_x, torque_z, torque_y)




    





