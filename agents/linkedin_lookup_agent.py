from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

    template = """
        Given the full name {name_of_person} I want you to get it me a link of their Linkedin profile page.
        Your answer should only contain a URL.
    """

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]

    return linkedin_profile_url
