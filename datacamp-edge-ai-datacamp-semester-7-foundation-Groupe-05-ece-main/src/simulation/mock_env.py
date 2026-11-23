"""Blank boilerplate for the text / PyBullet simulation (The Body, S7)."""


class MockEnv:
    """Minimal simulation interface. Swap for PyBullet / domain sim later."""

    def reset(self):
        """Return the initial observation."""
        raise NotImplementedError("Implement environment reset.")

    def step(self, action):
        """
        Apply an action and return (observation, reward, done, info).
        """
        raise NotImplementedError("Implement environment step.")
