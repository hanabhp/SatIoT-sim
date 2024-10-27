import pandas as pd
import matplotlib.pyplot as plt
import imageio
import numpy as np
import os

# Ensure output directories exist
os.makedirs("../visualization/plots", exist_ok=True)
os.makedirs("../visualization/animations", exist_ok=True)

def plot_doppler_shift(data):
    """
    Plot Doppler shifts over time for each satellite.
    """
    plt.figure(figsize=(10, 6))
    for satellite_id in data['satellite_id'].unique():
        subset = data[data['satellite_id'] == satellite_id]
        plt.plot(subset['time'], subset['Doppler_Shift'], label=f'Satellite {satellite_id}')

    plt.xlabel('Time (s)')
    plt.ylabel('Doppler Shift (Hz)')
    plt.title('Doppler Shift Over Time for Each Satellite')
    plt.legend(loc="upper right")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig("../visualization/plots/doppler_shift.png")
    plt.close()

def plot_coverage_area(data):
    """
    Plot coverage area for each satellite.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['satellite_id'], data['Coverage_Area_km2'], 'o-', color='orange')
    plt.xlabel('Satellite ID')
    plt.ylabel('Coverage Area (km²)')
    plt.title('Coverage Area per Satellite')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig("../visualization/plots/coverage_area.png")
    plt.close()

def create_trajectory_gif(data, output_filename="../visualization/animations/leo_trajectory.gif"):
    """
    Create an animated .gif to visualize LEO satellite trajectories over time.
    """
    frames = []
    for time in sorted(data['time'].unique()):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-1e7, 1e7)
        ax.set_ylim(-1e7, 1e7)
        subset = data[data['time'] == time]

        ax.plot(0, 0, 'o', color='blue', label='Earth')
        ax.scatter(subset['x'], subset['y'], s=50, c=subset['satellite_id'], cmap='viridis', label='Satellites')

        ax.set_title(f"LEO Satellite Trajectories at t={time} seconds")
        ax.legend()
        plt.grid(True, linestyle='--', alpha=0.7)

        # Save current figure to an in-memory buffer and add to frames list
        fig.canvas.draw()
        frame_image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        frame_image = frame_image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(frame_image)
        
        plt.close()

    # Save frames as a gif
    imageio.mimsave(output_filename, frames, fps=2)

# Main function to run visualizations
def run_visualizations():
    # Load data
    doppler_data = pd.read_csv("../data/combined_LEO_positions.csv")
    coverage_data = pd.read_csv("../data/LEO-Params.csv")
    trajectory_data = pd.read_csv("../data/combined_LEO_positions.csv")  # Assumes position data includes x, y, and time columns
    
    # Generate visualizations
    plot_doppler_shift(doppler_data)
    plot_coverage_area(coverage_data)
    create_trajectory_gif(trajectory_data)

if __name__ == "__main__":
    run_visualizations()

