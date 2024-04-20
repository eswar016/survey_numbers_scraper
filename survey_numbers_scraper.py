import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/knowLandStatus"
    data = {
        "distname": district,
        "mndname": mandal,
        "gpname": village
    }

    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')

    survey_numbers = []
    for option in soup.find("select", {"name": "surno"}).find_all("option"):
        survey_numbers.append(option.text.strip())

    return survey_numbers

if __name__ == "__main__":
    district = input("Enter district: ")
    mandal = input("Enter mandal: ")
    village = input("Enter village: ")

    survey_numbers = get_survey_numbers(district, mandal, village)
    print("Survey Numbers:")
    for number in survey_numbers:
        print(number)
