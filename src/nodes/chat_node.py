"""Node to handle chat interactions with the LLM."""

from pocketflow import Node
from constants import NodeState
from utils import call_llm


class ChatNode(Node):
    """Node to handle chat interactions with the LLM."""
    def prep(self, shared: dict):
        # Initialize messages if this is the first run
        if "messages" not in shared:
            shared["messages"] = []
            print("Welcome to the chat! Type 'exit' to end the conversation.")

        # Get user input
        user_input = input("\nYou: ")

        # Check if user wants to exit
        if user_input.lower() == 'exit':
            return NodeState.EXIT

        # Add user message to history
        shared["messages"].append({"role": "user", "content": user_input})

        # Return all messages for the LLM
        return shared["messages"]

    def exec(self, prep_res: list[dict[str, str]]):
        if prep_res == NodeState.EXIT:
            return NodeState.EXIT

        # Call LLM with the entire conversation history
        response = call_llm(prep_res)
        return response

    def post(self, shared: dict, prep_res: list[dict[str, str]], exec_res: str):
        if NodeState.EXIT in (prep_res, exec_res):
            print("\nGoodbye!")
            return NodeState.EXIT  # End the conversation

        # Print the assistant's response
        print(f"\nAssistant: {exec_res}")

        # Add assistant message to history
        shared["messages"].append({"role": "assistant", "content": exec_res})

        # Loop back to continue the conversation
        return NodeState.CONTINUE
