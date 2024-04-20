import requests

# Make a request to the URL
response = requests.get("https://dharani.telangana.gov.in/knowLandStatus")

# Print the response text
print(response.text)
