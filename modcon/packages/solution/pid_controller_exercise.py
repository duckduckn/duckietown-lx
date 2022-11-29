from typing import Tuple

import numpy as np


def PIDController(
        v_0: float,
        y_ref: float,
        y_hat: float,
        prev_e_y: float,
        prev_int_y: float,
        delta_t: float
) -> Tuple[float, float, float, float]:
    """
    PID performing lateral control.

    Args:
        v_0:        linear Duckiebot speed (given).
        y_ref:  reference heading pose.
        y_hat:  the current estiamted y.
        prev_e_y:     tracking error at previous iteration.
        prev_int_y:   previous integral error term.
        delta_t:    time interval since last call.

    Returns:
        v_0:     linear velocity of the Duckiebot
        omega:   angular velocity of the Duckiebot
        e:       current tracking error (automatically becomes prev_e_y at next iteration).
        e_int:   current integral error (automatically becomes prev_int_y at next iteration).
    """
    
 # TODO: these are random values, you have to implement your own PID controller in here
    omega = np.random.uniform(-8.0, 8.0)
    e = np.random.random()
    e_int = np.random.random()
    # ---
    
    return v_0, omega, e, e_int
