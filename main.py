import numpy as np
import time as t


if __name__ == "__main__":
    print("Starting calculations")
    starttime = t.time_ns()
    # call the functions here

    print("Calculations finished")
    time_taken = round((t.time_ns() - starttime)/1e9, 3)
    print("Took", time_taken, "seconds")


