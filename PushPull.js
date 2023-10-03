const axios = require('axios');


const api_key = 'INSIGHTS_KEY';
const event_type = 'CUSTOM_EVENT_TYPE';
const servicenow_url = 'https://<SERVICE_NOW_INSTANCE>.service-now.com/api/now/table/incident';
const servicenow_username = 'USERNAME';
const servicenow_password = 'PASSWORD';

axios.get(servicenow_url, {
  auth: {
    username: servicenow_username,
    password: servicenow_password,
  }
})
  .then((response) => {
    if (response.status === 200) {
      const incidents = response.data.result;

      for (const incident of incidents) {
        const payload = {
          eventType: event_type,
          incidentNumber: incident.number,
        };
        const headers = {
          'X-Insert-Key': api_key,
          'Content-Type': 'application/json',
        };
        const insights_url = 'https://insights-collector.newrelic.com/v1/accounts/ACCOUNT/events';

        axios.post(insights_url, payload, { headers })
          .then((insights_response) => {
            if (insights_response.status === 200) {
              console.log('Data Pushed');
            } else {
              console.log('Failed to push data to New Relic Insights. Status code:', insights_response.status);
            }
          })
          .catch((error) => {
            console.error('Error pushing data to New Relic Insights:', error);
          });
      }
    } else {
      console.error('Failed to fetch data from ServiceNow. Status code:', response.status);
    }
  })
  .catch((error) => {
    console.error('Error fetching data from ServiceNow:', error);
  });
