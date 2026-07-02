import numpy as np

def calculate_heat_transfer(flow_rate, cp, hot_in, hot_out):
    return flow_rate * cp * (hot_in - hot_out)


def calculate_lmtd(hot_in, hot_out, cold_in, cold_out):

    delta1 = hot_in - cold_out
    delta2 = hot_out - cold_in

    if delta1 == delta2:
        return delta1

    return (delta1 - delta2) / np.log(delta1 / delta2)


def calculate_effectiveness(
    hot_in,
    hot_out,
    cold_in
):

    return (hot_in - hot_out) / (hot_in - cold_in)