import numpy as np

class Environment:
    # The environment.
    #
    # === Attributes ===
    # grid: The grid representing the environment. A 0 represents an empty
    #   spot, a 1 represents a piece of trash
    def __init__(self):
        # Initializes a new random environment.
        self.grid = np.random.randint(2, size = (100, 100))
