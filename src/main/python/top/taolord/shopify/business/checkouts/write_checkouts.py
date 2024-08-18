import requests

class WriteCheckouts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_checkout(self, checkout_data):
        """Send a POST request to create or update a checkout."""
        url = f'{self.base_url}/checkouts.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'checkout': checkout_data})
        if response.status_code == 201:
            return response.json().get('checkout', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_checkout(self, checkout_data):
        """Create a new checkout."""
        return self._post_checkout(checkout_data)

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteCheckouts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new checkout
    checkout_data = {
        'line_items': [
            {
                'variant_id': 123456789,
                'quantity': 1
            }
        ],
        'customer': {
            'id': 987654321
        },
        'shipping_address': {
            'address1': '123 Example St',
            'city': 'Sample City',
            'province': 'Sample State',
            'country': 'US',
            'zip': '12345'
        },
        'email': 'customer@example.com'
        # Add other required fields here
    }

    created_checkout = writer.create_checkout(checkout_data)

    print(created_checkout)
