def calculate_bottom_product(feed_flow, distillate_flow):
    return feed_flow - distillate_flow


def calculate_recovery(feed_flow, distillate_flow):
    return (distillate_flow / feed_flow) * 100


def calculate_separation_efficiency(top_purity, bottom_purity):
    return ((top_purity + bottom_purity) / 2)


def calculate_reflux_ratio(reflux, distillate):
    return reflux / distillate