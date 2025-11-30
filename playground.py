from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY not found. Please check your .env file.")

# Model Definition
groq_model = Groq(id="llama-3.3-70b-versatile")

# 1. Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True,
)

# 2. Financial Agent
finance_agent = Agent(
    name="Financial Agent",
    role="Financial data analyst",
    model=groq_model,
    tools=[
        YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            stock_fundamentals=True,
            company_info=True, 
            company_news=True
        )
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# 3. Multi-Agent Team 
multi_ai_agent = Agent(
    name="Super Financial Team",
    role="Leader of the Finance and News Team",
    team=[web_search_agent, finance_agent],
    model=groq_model,
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Playground Application
app = Playground(agents=[web_search_agent, finance_agent, multi_ai_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)