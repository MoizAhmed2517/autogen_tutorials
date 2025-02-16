import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
load_dotenv()

llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY_V1"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about NVIDA and TESLA stock prices.",
)