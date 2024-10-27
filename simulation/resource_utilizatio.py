def calculate_channel_utilization(leo_positions, config):
    """
    Calculate the channel utilization for the entire communication network.

    Parameters:
        leo_positions: DataFrame containing LEO satellite data and transmission times
        config: Configuration dictionary with simulation and channel parameters

    Returns:
        channel_utilization: The calculated channel utilization as a percentage
    """
    # Total simulation time in seconds
    T_total = config["simulation_time"]

    # Calculate total transmission time for all packets
    total_transmission_time = leo_positions["Transmission_Time"].sum()

    # Channel utilization as the fraction of time the channel is used
    channel_utilization = (total_transmission_time / T_total) * 100  # As a percentage
    return channel_utilization


def calculate_energy_efficiency(leo_positions, config):
    """
    Calculate the energy efficiency of the communication network.

    Parameters:
        leo_positions: DataFrame containing LEO satellite data and effective throughput
        config: Configuration dictionary with power consumption parameters

    Returns:
        energy_efficiency: Energy efficiency as effective throughput per unit of power
    """
    # Calculate effective throughput (sum of successful data packets in bits)
    effective_throughput = leo_positions["Effective_Throughput"].sum()

    # Total power consumption over simulation (power per satellite * number of satellites)
    power_per_satellite = config["power_consumption_per_satellite"]  # Watts
    num_satellites = config["num_leo_satellites"]
    total_power = power_per_satellite * num_satellites * config["simulation_time"]  # in Joules (W*s)

    # Energy efficiency as throughput per unit of power (bits per Joule)
    energy_efficiency = effective_throughput / total_power
    return energy_efficiency

