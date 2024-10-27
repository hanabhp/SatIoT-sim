import math

def calculate_end_to_end_delay(row, config):
    """
    Calculate the end-to-end delay for communication from an IoT device to a satellite.

    Parameters:
        row: Data row containing distance and other parameters
        config: Configuration dictionary with delay parameters

    Returns:
        end_to_end_delay: Total delay in seconds
    """
    
    # Propagation Delay (Tprop): d/c
    d = row["distance_to_device"]  # Distance between device and satellite in meters
    c = config["speed_of_light"]   # Speed of light in m/s
    Tprop = d / c

    # Processing Delay (Tproc): Sum of satellite and gateway processing times
    Tproc = config["processing_delay"]["satellite"] + config["processing_delay"]["gateway"]
    
    # Queuing Delay (Tqueue) using M/M/1 queue model: ρ / μ(1 - ρ)
    ρ = config["queue_parameters"]["utilization_factor"]  # Utilization factor
    μ = config["queue_parameters"]["service_rate"]        # Service rate (packets per second)
    Tqueue = ρ / (μ * (1 - ρ)) if ρ < 1 else float('inf')  # Avoid division by zero if utilization is 100%
    
    # Transmission Delay (Ttx): Packet size / data rate
    packet_size = config["packet_size"]  # Packet size in bits
    data_rate = config["data_rate"]      # Data rate in bits per second
    Ttx = packet_size / data_rate
    
    # Total End-to-End Delay
    end_to_end_delay = Tprop + Tproc + Tqueue + Ttx
    return end_to_end_delay

