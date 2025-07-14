import streamlit as st
import os
from src.langgrap_chatbot_app.UI.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_stramlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),
            layout='wide'
        )
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Load options from Config file
            llm_options = self.config.get_llm_options()
            usecase_option = self.config.usecase_options()

            # LLM Selection
            self.user_controls['llm'] = st.selectbox(
                "Select LLM",
                llm_options,
            )

            if self.user_controls['llm'] == 'Groq':
                # Selecting and Loading the model
                model_options = self.config.get_groq_model_options()
                self.user_controls['model'] = st.selectbox(
                    "Select Groq Model",
                    model_options,
                )
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "API Key", type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(
                        "⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            # Usecase Selection
            self.user_controls['usecase'] = st.selectbox(
                "Select Usecase",
                usecase_option,
            )

        return self.user_controls
