from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")


def GeminiCall(user, llmIn=llm):
    print()
    try:
        prompt = "You are a pandas query generator to generator or correct the pandas query based on the the following input "+"'"+user+"'"
        result = llmIn.invoke(prompt)

        # print(result.content)
        # print(type(result.content))
        return result.content
    except Exception as e:
        # print(e.args[0])
        return e.args[0]

