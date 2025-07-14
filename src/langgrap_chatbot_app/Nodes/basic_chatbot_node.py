from src.langgrap_chatbot_app.State.state import State


class BasicChatbotNode:
    """
    A basic chatbot node that processes messages and returns a response.
    """

    def __init__(self, model):
        self.llm = model

    def process_message(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        # Here you can implement your logic to generate a response
        return {"messages": self.llm.invoke(state['messages'])}