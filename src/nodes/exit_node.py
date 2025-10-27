"""Node to handle exiting the chat."""

from pocketflow import Node
from constants import NodeState

class ExitNode(Node):
    """Node to handle exiting the chat."""
    def prep(self, shared: dict):
        print("\nExiting the chat. Have a great day!")
        return NodeState.EXIT

    def exec(self, prep_res):
        return NodeState.EXIT

    def post(self, shared: dict, prep_res, exec_res):
        return NodeState.EXIT
