
import time
from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import sys 
import os
from langchain_mistralai import ChatMistralAI
import time
import dotenv
dotenv.load_dotenv()
from combinedPrompts import system_prompt
# Having a system path so that the files are all readable
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from tools.utility import tools
from utils.utils import AgentState

class Agent(): 
    def __init__(self):
        self.mistral_model = ChatMistralAI(model="mistral-large-latest", temperature=0, api_key=os.getenv("MISTRAL_API_KEY"))
        Tool = tools()
        self.tools = Tool.toolkit()
        self.model_with_tool = self.mistral_model.bind_tools(self.tools)
    def run_agent(self, state: AgentState, config: RunnableConfig) -> dict:
        time.sleep(3)
        model = self.mistral_model.bind_tools([tools])
        resume_and_jd = state["messages"][-1].content
        print(f"Resume and JD: {resume_and_jd}")
        prompt = system_prompt(resume_and_jd)
        response = self.model_with_tool.invoke([prompt] + state["messages"], config)        
        return {"messages": [response]}

