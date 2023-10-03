import requests

api_key = 'INSIGHTS_KEY'
event_type = 'CUSTOM_EVENT_TYPE'

payload = {
    'eventType': event_type,
}

headers = {
            'X-Insert-Key': api_key,
            'Content-Type': 'application/json',
        }

insights_url = 'https://insights-collector.newrelic.com/v1/accounts/<ACCOUNT NO>/events'
insights_response = requests.post(insights_url, headers=headers, json=payload)