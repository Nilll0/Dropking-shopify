import requests

class WriteShipping:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_shipping(self, shipping_data):
        """Send a POST request to create shipping data."""
        url = f'{self.base_url}/shipping.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'shipping': shipping_data})
        if response.status_code == 201:
            return response.json().get('shipping', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_shipping(self, shipping_data):
        """Create new shipping data."""
        return self._post_shipping(shipping_data)

    def update_shipping(self, shipping_id, shipping_data):
        """Update existing shipping data."""
        url = f'{self.base_url}/shipping/{shipping_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'shipping': shipping_data})
        if response.status_code == 200:
            return response.json().get('shipping', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteShipping(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create new shipping data
    shipping_data = {
        'title': 'New Shipping Option',
        'rate': '5.00',
        'service': 'Standard Shipping'
        # Add other fields as required by your use case
    }

    created_shipping = writer.create_shipping(shipping_data)
    print('Created Shipping:', created_shipping)

    # Example data to update existing shipping data
    shipping_id = created_shipping.get('id')
    updated_shipping_data = {
        'title': 'Updated Shipping Option Title'
        # Add other fields to update as necessary
    }

    updated_shipping = writer.update_shipping(shipping_id, updated_shipping_data)
    print('Updated Shipping:', updated_shipping)
