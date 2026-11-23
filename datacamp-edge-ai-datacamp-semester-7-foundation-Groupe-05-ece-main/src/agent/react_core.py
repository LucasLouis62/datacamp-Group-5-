"""Blank boilerplate for the main ReAct reasoning loop (The Brain)."""


def react_step(observation, history=None):
    """
    One Observe → Think → Act cycle.

    Returns:
        dict: proposed action (to be checked by the Guardian before execution).
    """
    raise NotImplementedError("Implement the ReAct reasoning loop here.")
