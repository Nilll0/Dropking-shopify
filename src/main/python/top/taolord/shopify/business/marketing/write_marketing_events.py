import requests

class WriteMarketingEvents:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_marketing_event(self, marketing_event_data):
        """Send a POST request to create a marketing event."""
        url = f'{self.base_url}/marketing_events.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'marketing_event': marketing_event_data})
        if response.status_code == 201:
            return response.json().get('marketing_event', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_marketing_event(self, marketing_event_data):
        """Create a new marketing event."""
        return self._post_marketing_event(marketing_event_data)

    def update_marketing_event(self, marketing_event_id, marketing_event_data):
        """Update an existing marketing event."""
        url = f'{self.base_url}/marketing_events/{marketing_event_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'marketing_event': marketing_event_data})
        if response.status_code == 200:
            return response.json().get('marketing_event', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteMarketingEvents(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new marketing event
    marketing_event_data = {
        'title': 'Summer Sale',
        'description': 'Discounts on summer collection.',
        'start_at': '2024-08-01T00:00:00Z',
        'end_at': '2024-08-31T23:59:59Z',
        'type': 'sale'
    }

    created_marketing_event = writer.create_marketing_event(marketing_event_data)
    print('Created Marketing Event:', created_marketing_event)

    # Example data to update an existing marketing event
    marketing_event_id = created_marketing_event.get('id')
    updated_marketing_event_data = {
        'title': 'Extended Summer Sale'
        # Add other fields to update as necessary
    }

    updated_marketing_event = writer.update_marketing_event(marketing_event_id, updated_marketing_event_data)
    print('Updated Marketing Event:', updated_marketing_event)
