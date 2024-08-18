import requests

class WritePaymentGateways:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_payment_gateway(self, gateway_data):
        """Send a POST request to create a payment gateway."""
        url = f'{self.base_url}/payment_gateways.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'payment_gateway': gateway_data})
        if response.status_code == 201:
            return response.json().get('payment_gateway', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_payment_gateway(self, gateway_data):
        """Create a new payment gateway."""
        return self._post_payment_gateway(gateway_data)

    def update_payment_gateway(self, gateway_id, gateway_data):
        """Update an existing payment gateway."""
        url = f'{self.base_url}/payment_gateways/{gateway_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'payment_gateway': gateway_data})
        if response.status_code == 200:
            return response.json().get('payment_gateway', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WritePaymentGateways(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new payment gateway
    gateway_data = {
        'name': 'New Payment Gateway',
        'provider_id': 'new-provider-id',
        'enabled': True
        # Add other required fields as necessary
    }

    created_gateway = writer.create_payment_gateway(gateway_data)
    print('Created Payment Gateway:', created_gateway)

    # Example data to update an existing payment gateway
    gateway_id = created_gateway.get('id')
    updated_gateway_data = {
        'enabled': False
        # Add other fields to update as necessary
    }

    updated_gateway = writer.update_payment_gateway(gateway_id, updated_gateway_data)
    print('Updated Payment Gateway:', updated_gateway)
