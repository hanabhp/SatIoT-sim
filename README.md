# Satellite-IoT Communication Simulation 🚀

## Overview
This project simulates LoRa-based satellite-IoT communication systems, focusing on LEO and GEO satellite architectures. It models key metrics such as Doppler shift, link budget, delay, coverage, and resource utilization under different scenarios. The modular structure provides flexibility for various configurations and performance evaluations.

## Project Structure
```
sat_iot_simulation/
├── config/
│   └── simulation_config.json          # Configurable simulation parameters
├── data/
│   ├── combined_LEO_positions.csv      # LEO satellite trajectory data
│   ├── SITES-LLA-Pos.csv              # IoT ground sites (Latitude, Longitude, Altitude format)
│   ├── SITES-XYZ-Pos.csv              # IoT ground sites (Cartesian coordinates)
│   ├── GW-Pos.csv                     # Gateway positions
│   └── LEO-Params.csv                 # LEO satellite parameters
├── logs/
│   └── latest_run.log                 # Log file for each simulation run
├── simulation/
│   ├── main_simulation.py             # Main script to orchestrate the simulation
│   ├── doppler_calculations.py        # Calculates Doppler effect
│   ├── link_budget.py                 # Link budget calculations with Doppler impact
│   ├── delay_analysis.py              # Calculates end-to-end delay
│   ├── coverage_analysis.py           # Calculates satellite coverage area
│   └── resource_utilization.py        # Computes channel utilization and energy efficiency
├── visualization/
│   ├── plots/                         # Visualizations of delay, coverage, Doppler effects
│   └── animations/                    # .gif animations for satellite and IoT movements
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Ignores unnecessary files
└── run_simulation.py                  # Runs the simulation, data logging, and visualizations
```

## Installation and Setup
### Prerequisites
- Python 3.8 or higher
- Libraries specified in requirements.txt

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/your-username/sat_iot_simulation.git
cd sat_iot_simulation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Adjust simulation parameters in `config/simulation_config.json`:
- Simulation Settings: simulation_time, num_leo_satellites, num_iot_devices
- LoRa Parameters: spreading_factor, bandwidth, transmission_power, coding_rate
- Physical Constants: gravitational_constant, earth_mass, earth_radius, speed_of_light
- Satellite Altitudes: leo_altitude, geo_altitude
- Scenario-Specific Parameters: dense_urban_iot, rural_remote_iot, mobile_iot

## Running the Simulation
Execute the main script:
```bash
python run_simulation.py
```

## Outputs
- Logs: Results stored in `logs/latest_run.log`
- Visualizations: Generated in `visualization/` directory


###  Collaborating Institutions:
- **University of California, Berkeley, INRIA (FRANCE), CNRS (France).

### 🤝 Open for Collaboration

---

### Contact
**Email**: h.pasandi@berkeley.edu

---



