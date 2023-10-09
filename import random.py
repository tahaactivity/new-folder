import random

def simulate_radiation_exposure(half_life, num_trials):
    """
    Simulate radiation exposure for a given number of trials.

    Args:
    - half_life: The half-life of the radioactive substance (time it takes for half of the substance to decay).
    - num_trials: The number of trials or time steps to simulate.

    Returns:
    - Total radiation exposure over the specified number of trials.
    """
    radiation_exposure = 0.0

    for _ in range(num_trials):
        if random.random() < 0.5:
            radiation_exposure += 1.0
        half_life -= 1  # Reduce the remaining half-life by 1 time step
        if half_life <= 0:
            break  # Stop the simulation when the half-life is exhausted

    return radiation_exposure

# Example usage
half_life = 50  # Replace with the actual half-life of the substance
num_trials = 10000  # Number of time steps to simulate
total_exposure = simulate_radiation_exposure(half_life, num_trials)
print(f"Total radiation exposure: {total_exposure} units")
