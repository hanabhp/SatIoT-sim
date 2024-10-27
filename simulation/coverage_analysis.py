import math

def calculate_coverage_area(row, config):
    """
    Calculate the coverage area on Earth's surface for a satellite.

    Parameters:
        row: Data row containing satellite altitude and other parameters
        config: Configuration dictionary with Earth radius and satellite altitude

    Returns:
        coverage_area: Coverage area in square kilometers
    """
    
    # Earth radius and satellite altitude
    RE = config["earth_radius"]  # Radius of Earth in meters
    h = row["altitude"]          # Satellite altitude in meters
    
    # Maximum elevation angle for coverage
    theta_max = math.acos(RE / (RE + h))  # radians
    
    # Coverage Area (A): 2π * RE^2 * (1 - cos(θ_max))
    coverage_area = 2 * math.pi * (RE ** 2) * (1 - math.cos(theta_max))
    
    # Convert to square kilometers
    coverage_area_km2 = coverage_area / 1e6
    return coverage_area_km2

