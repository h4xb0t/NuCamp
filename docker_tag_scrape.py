#!/usr/bin/env python
from requests import get
import getpass

admin_pass = getpass.getpass("Password: ")

api_query = input("Enter API URL to query: ")
response = get(api_query,
               auth=('admin', admin_pass))

json_response = response.json()

tag_list = json_response['tags']

print(f"The tag total is {len(tag_list)}")
