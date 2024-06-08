from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")


def GeminiCall(df,user, llmIn=llm):
    print()
    try:
        agent_executor = create_pandas_dataframe_agent(
                llmIn,
                df,
                agent_type="zero-shot-react-description",
                verbose=True,
                return_intermediate_steps=True
        )
        # prompt = "You are a pandas query generator to generator or correct the pandas query based on the the following input "+"'"+user+"'"
        # result = llmIn.invoke(prompt)

        result = agent_executor.invoke(user)

        # print("IN")

        # print(result['output'])
        # print(type(result.output))
        return result['output']
    except Exception as e:
        # print(e.args[0])
        return e.args[0]

