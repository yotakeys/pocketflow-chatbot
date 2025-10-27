"""Constants for node states in the chatbot flow."""

from enum import Enum

class NodeState(str, Enum):
    """Enumeration for different states of a node."""
    CONTINUE = "continue"
    EXIT = "exit"
