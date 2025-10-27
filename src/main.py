"""Main entry point for the chatbot application."""
from flows import FlowChat

# Start the chat
if __name__ == "__main__":
    data = {}
    flow = FlowChat()
    flow.run(data)
    print(data)
