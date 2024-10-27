import json
import pandas as pd
import logging
import os
from doppler_calculations import calculate_doppler_shift
from link_budget import compute_link_budget
from delay_analysis import calculate_end_to_end_delay
from coverage_analysis import calculate_coverage_area
from resource_utilization import calculate_channel_utilization, calculate_energy_efficiency

# Ensure the logs directory exists
os.makedirs("../logs", exist_ok=True)

# Configure logging to write to latest_run.log
logging.basicConfig(
    filename="../logs/latest_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load configuration
with open("../config/simulation_config.json", "r") as config_file:
    config = json.load(config_file)

# Load data
leo_positions = pd.read_csv("../data/combined_LEO_positions.csv")
sites_lla = pd.read_csv("../data/SITES-LLA-Pos.csv")
sites_xyz = pd.read_csv("../data/SITES-XYZ-Pos.csv")
gateway_positions = pd.read_csv("../data/GW-Pos.csv")

def run_simulation():
    logging.info("Starting new simulation run")

    # Step 1: Calculate Doppler effect for each LEO satellite
    logging.info("Calculating Doppler shifts for all satellites")
    leo_positions['Doppler_Shift'] = leo_positions.apply(
        lambda row: calculate_doppler_shift(row, config), axis=1)

    # Step 2: Compute link budget including Doppler impact
    logging.info("Computing link budgets with Doppler impact")
    leo_positions['Link_Budget'] = leo_positions.apply(
        lambda row: compute_link_budget(row, config), axis=1)

    # Step 3: Calculate end-to-end delay
    logging.info("Calculating end-to-end delays for each satellite-to-device link")
    leo_positions['End_to_End_Delay'] = leo_positions.apply(
        lambda row: calculate_end_to_end_delay(row, config), axis=1)

    # Step 4: Calculate coverage area based on satellite altitude and elevation angle
    logging.info("Calculating coverage areas for all satellites")
    leo_positions['Coverage_Area_km2'] = leo_positions.apply(
        lambda row: calculate_coverage_area(row, config), axis=1)
    total_coverage_area = leo_positions['Coverage_Area_km2'].sum()
    logging.info(f"Total Coverage Area: {total_coverage_area} km^2")

    # Step 5: Calculate channel utilization and energy efficiency
    logging.info("Calculating channel utilization")
    channel_utilization = calculate_channel_utilization(leo_positions, config)
    logging.info(f"Channel Utilization: {channel_utilization:.2f}%")

    logging.info("Calculating energy efficiency of the communication network")
    energy_efficiency = calculate_energy_efficiency(leo_positions, config)
    logging.info(f"Energy Efficiency: {energy_efficiency:.2f} bits per Joule")

    logging.info("Simulation completed successfully")

if __name__ == "__main__":
    try:
        run_simulation()
    except Exception as e:
        logging.error(f"An error occurred during the simulation: {e}")

