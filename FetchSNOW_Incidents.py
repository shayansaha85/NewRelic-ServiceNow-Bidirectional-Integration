import requests


servicenow_url = 'https://<SERVICE_NOW_INSTANCE>.service-now.com/api/now/table/incident'
servicenow_username = 'USERNAME'
servicenow_password = 'PASSWORD'

response = requests.get(servicenow_url, auth=(servicenow_username, servicenow_password))

