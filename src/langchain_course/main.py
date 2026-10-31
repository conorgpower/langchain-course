from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavily = TavilyClient()
TavilySearch

llm = ChatOpenAI(model="gpt-6.1-terra")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an AI engineer using langchain in the dubai area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()