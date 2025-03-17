from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import pandas as pd
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

llm = init_chat_model("gemini-2.0-flash-001", model_provider="google_vertexai")
# llm = ChatGoogleGenerativeAI(model="gemini-pro")

def GeminiCall(df, user, llmIn=llm):
    print()
    try:
        agent_executor = create_pandas_dataframe_agent(
            llmIn,
            df,
            agent_type="zero-shot-react-description",
            verbose=True,
            return_intermediate_steps=True,
            allow_dangerous_code=True,
        )
        result = agent_executor.invoke({"input":user})

        return result['output']
    except Exception as e:
        return str(e)
