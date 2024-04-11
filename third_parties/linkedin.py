import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("RAPIDAPI_LINKEDIN_API_KEY")


def scrape_linkedin_data(profile_url):
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
    querystring = {"linkedin_url": profile_url, "include_skills": "true"}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    resp_data = response.json()["data"]
    profile = {
        i: resp_data[i]
        for i in resp_data
        if resp_data[i]
        not in [
            None,
            "",
            [],
            "urn",
            "company_logo_url",
            "company_website",
            "company_linkedin_url",
        ]
    }

    return profile


def scrape_linkedin_data_mock():
    response = requests.get(
        "https://gist.githubusercontent.com/kknamish/d7aba74a78fcbc31399af146de9bc125/raw/bb48cdfee4ec993d653fee15a437ce824ae6799d/linkedin_profile.json"
    )
    resp_data = response.json()["data"]
    profile = {
        i: resp_data[i]
        for i in resp_data
        if resp_data[i]
        not in [
            None,
            "",
            [],
            "urn",
            "company_logo_url",
            "company_website",
            "company_linkedin_url",
        ]
    }

    return profile


scrape_linkedin_data_mock()
