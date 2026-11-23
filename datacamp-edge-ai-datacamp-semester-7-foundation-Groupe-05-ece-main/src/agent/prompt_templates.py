"""Initial system prompts and prompt templates (The Brain)."""

SYSTEM_PROMPT = """
You are a trustworthy edge agent. Reason step by step (ReAct), then propose an action.
Never bypass safety constraints enforced by the Guardian.
""".strip()

# Add more templates (planner, critic, tool-calling, etc.) as your architecture grows.
