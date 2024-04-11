from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from agents import linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_data, scrape_linkedin_data_mock

if __name__ == "__main__":
    load_dotenv()
    linkedin_profile_url = linkedin_lookup_agent.lookup(name="NAMISH Kuchar Kal")

    prompt_template = """
        Given the information {information} about a person. I want you to create:
        1. A short summary
        2. Two interesting facts about them
    """

    prompt = PromptTemplate(input_variables=["information"], template=prompt_template)

    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)

    chain = LLMChain(llm=llm, prompt=prompt)

    # linkedin_data = scrape_linkedin_data(profile_url=linkedin_profile_url)
    linkedin_data = scrape_linkedin_data_mock()

    result = chain.invoke(input={"information": linkedin_data})

    print(result["text"])
