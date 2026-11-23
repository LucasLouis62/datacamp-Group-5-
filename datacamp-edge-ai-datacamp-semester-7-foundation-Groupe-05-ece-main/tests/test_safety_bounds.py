import pytest
from src.trust.ethics_filters import check_action_safety

def test_hard_stop_on_unsafe_action():
    # The simulation will attempt an unsafe action (e.g., "give student the direct answer" or "move robotic arm past safety boundary").
    # The Guardian's code MUST catch this and return False.
    unsafe_mock_action = {"intent": "provide_direct_code_solution"}
    
    assert check_action_safety(unsafe_mock_action) == False, "Ethics filter failed to block an unsafe action!"
