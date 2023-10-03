import requests

api_key = 'INSIGHTS_KEY'
event_type = 'CUSTOM_EVENT_TYPE'

servicenow_url = 'https://<SERVICE_NOW_INSTANCE>.service-now.com/api/now/table/incident'
servicenow_username = 'USERNAME'
servicenow_password = 'PASSWORD'

response = requests.get(servicenow_url, auth=(servicenow_username, servicenow_password))

if response.status_code == 200:
    incidents = response.json().get('result')

    
    for incident in incidents:
        payload = {
            'eventType': event_type,
            'incidentNumber': incident['number'],
        }
        headers = {
            'X-Insert-Key': api_key,
            'Content-Type': 'application/json',
        }
        insights_url = 'https://insights-collector.newrelic.com/v1/accounts/ACCOUNT/events'
        insights_response = requests.post(insights_url, headers=headers, json=payload)
        if insights_response.status_code == 200:
            print("Data Pushed")
        else:
            print("Data Pushed")
else:
    print(f"Failed to fetch data from ServiceNow. Status code: {response.status_code}")
