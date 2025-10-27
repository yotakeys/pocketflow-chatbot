"""Flow for handling chat interactions."""

from pocketflow import Flow
from constants import NodeState
from nodes import ChatNode, ExitNode

class FlowChat(Flow):
    """Flow for handling chat interactions."""
    def __init__(self):
        chat_node = ChatNode()
        exit_node = ExitNode()

        # Define transitions
        chat_node - NodeState.CONTINUE >> chat_node
        chat_node - NodeState.EXIT >> exit_node

        super().__init__(start=chat_node)
