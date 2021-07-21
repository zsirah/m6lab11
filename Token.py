import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

un = input("Enter your username: ")
pw = getpass("Enter your password: ")

ciscoURL = "https://sandboxdnac.cisco.com"
tokenPath = "/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

TA = ciscoURL + tokenPath

response = requests.post(TA, auth=HTTPBasicAuth(un, pw), headers=headers, data=payload)

Auth_Token = response.json()

Token = Auth_Token['Token']

print("Token retrieved successfully. The token value is as follows:\n" + Token)

