def calculate_conversion(feed, product):
    return (product / feed) * 100


def calculate_yield(product, theoretical):
    return (product / theoretical) * 100


def calculate_selectivity(desired, undesired):
    return desired / undesired


def calculate_residence_time(volume, flow_rate):
    return volume / flow_rate