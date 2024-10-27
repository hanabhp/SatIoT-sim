import math

def compute_link_budget(row, config):
    """
    Calculate the link budget for a LEO satellite communication link,
    accounting for Doppler-induced degradation.

    Parameters:
        row: Data row containing satellite position, Doppler shift, etc.
        config: Configuration dictionary with link budget constants

    Returns:
        link_budget: The computed link budget in dB
    """
    
    # Load parameters from config and data row
    Pt = config["lora_parameters"]["transmission_power"]  # Transmit power (dBm)
    Gt = config["gateway_gain"]  # Transmit antenna gain (dBi) for gateway
    Gr = config["satellite_gain"]  # Receive antenna gain (dBi) for satellite
    f_d = row["Doppler_Shift"]  # Doppler shift calculated in doppler_calculations.py
    BW = config["lora_parameters"]["bandwidth"]  # Bandwidth in Hz
    d = row["distance_to_device"]  # Distance between satellite and device in meters
    c = config["speed_of_light"]  # Speed of light (m/s)

    # Calculate Free Space Path Loss (Lf_s) in dB
    Lf_s = 20 * math.log10(d) + 20 * math.log10(config["carrier_frequency"]) - 20 * math.log10(c)
    
    # Atmospheric Loss (Latm)
    Latm = config.get("atmospheric_loss", 2)  # Default to 2 dB if not specified

    # Doppler-induced degradation (Ld) in dB
    Ld = 20 * math.log10(1 + f_d / BW)
    
    # Calculate link budget
    link_budget = Pt + Gt + Gr - Lf_s - Latm - Ld
    return link_budget

