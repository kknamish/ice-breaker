from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


if __name__ == "__main__":
    load_dotenv()

    information = """
        Mahendra Singh Dhoni (/məˈheɪndrə ˈsɪŋ dhæˈnɪ/ ⓘ; born 7 July 1981) is an Indian professional cricketer. 
        He is a right handed batter and a wicket-keeper. Widely regarded as one of the most prolific 
        wicket-keeper-batsmen and captains, he represented the Indian cricket team and was the captain of the side in 
        limited-overs formats from 2007 to 2017 and in test cricket from 2008 to 2014. Dhoni has captained the most 
        international matches and is the most successful Indian captain. He has led India to victory in the 2011 Cricket 
        World Cup, the 2007 ICC World Twenty20 and the 2013 ICC Champions Trophy, the only captain to win three 
        different limited overs tournaments. He also led the teams that won the Asia Cup in 2010, 2016 and was a member 
        of the title winning squad in 2018.
    """

    prompt_template = """
        Given the information {information} about a person. I want you to create:
        1. A short summary
        2. Two interesting facts about them
    """

    prompt = PromptTemplate(input_variables=["information"], template=prompt_template)

    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)

    chain = LLMChain(llm=llm, prompt=prompt)

    result = chain.invoke(input={"information": information})

    print(result['text'])
