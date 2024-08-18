import requests

class WriteFulfillments:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_fulfillment(self, fulfillment_data):
        """Send a POST request to create or update a fulfillment."""
        url = f'{self.base_url}/fulfillments.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'fulfillment': fulfillment_data})
        if response.status_code == 201:
            return response.json().get('fulfillment', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_fulfillment(self, fulfillment_data):
        """Create a new fulfillment."""
        return self._post_fulfillment(fulfillment_data)

    def update_fulfillment(self, fulfillment_id, fulfillment_data):
        """Update an existing fulfillment."""
        url = f'{self.base_url}/fulfillments/{fulfillment_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'fulfillment': fulfillment_data})
        if response.status_code == 200:
            return response.json().get('fulfillment', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteFulfillments(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new fulfillment
    fulfillment_data = {
        'order_id': 123456789,
        'location_id': 987654321,
        'tracking_number': '1234567890',
        'tracking_urls': ['https://example.com/track/1234567890'],
        'line_items': [
            {
                'id': 111111111,
                'quantity': 1
            }
        ]
        # Add other required fields here
    }

    created_fulfillment = writer.create_fulfillment(fulfillment_data)
    print('Created Fulfillment:', created_fulfillment)

    # Example data to update an existing fulfillment
    fulfillment_id = created_fulfillment.get('id')
    updated_fulfillment_data = {
        'tracking_number': '0987654321'
        # Add other fields to update as necessary
    }

    updated_fulfillment = writer.update_fulfillment(fulfillment_id, updated_fulfillment_data)
    print('Updated Fulfillment:', updated_fulfillment)
