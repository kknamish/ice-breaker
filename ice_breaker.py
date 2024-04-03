from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from third_parties.linkedin import scrape_linkedin_data

if __name__ == "__main__":
    load_dotenv()

    information = scrape_linkedin_data(profile_url="")

    prompt_template = """
        Given the information {information} about a person. I want you to create:
        1. A short summary
        2. Two interesting facts about them
    """

    prompt = PromptTemplate(input_variables=["information"], template=prompt_template)

    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)

    chain = LLMChain(llm=llm, prompt=prompt)

    result = chain.invoke(input={"information": information})

    print(result["text"])
