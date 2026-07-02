def calculate_efficiency(temperature, pressure):
    efficiency = (temperature / pressure) * 100
    return efficiency

def calculate_energy(temperature, flow_rate):
    energy = temperature * flow_rate
    return energy

def calculate_heat_duty(temperature, flow_rate):
    """
    Simplified heat duty 
    Q = m * Cp * delT
    
    Assume: 
    Cp = 4.18 kJ/kg C

    """
    cp = 4.18
    heat_duty = flow_rate * cp * temperature
    return heat_duty

def calculate_operating_cost(energy):
    cost_per_kg = 0.05
    return energy * cost_per_kg

