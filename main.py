import time as t

import fns
import inputvars


if __name__ == "__main__":
    print("Starting calculations")
    starttime = t.time_ns()
    # call the functions here

    orbitalperiod = fns.get_orbital_period(inputvars.mercury_grav_parameter, inputvars.final_sma)
    orbitalfrequency = 1/orbitalperiod
    rot_degrees_p_sec = 360 * orbitalfrequency
    print("orbital period =", orbitalperiod)
    print("rotational speed in deg/s =", rot_degrees_p_sec)

    print("Calculations finished")
    time_taken = round((t.time_ns() - starttime)/1e9, 3)
    print("Took", time_taken, "seconds")


