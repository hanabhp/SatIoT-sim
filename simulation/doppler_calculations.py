import math

def calculate_doppler_shift(row, config):
    """
    Calculate the Doppler shift for a LEO satellite relative to an IoT device.
    
    Parameters:
        row: Data row containing satellite position and velocity
        config: Configuration dictionary with required constants

    Returns:
        Doppler shift in Hz
    """
    fc = config["carrier_frequency"]  # Carrier frequency in Hz
    vs = row["velocity"]  # Satellite speed in m/s
    theta = math.radians(row["elevation_angle"])  # Elevation angle in radians
    c = 3e8  # Speed of light in m/s
    
    # Doppler shift calculation
    doppler_shift = fc * (vs * math.cos(theta)) / c
    return doppler_shift

