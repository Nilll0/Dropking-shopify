import requests

class WritePaymentMandate:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_payment_mandate(self, mandate_data):
        """Send a POST request to create a payment mandate."""
        url = f'{self.base_url}/payment_mandates.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'payment_mandate': mandate_data})
        if response.status_code == 201:
            return response.json().get('payment_mandate', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_payment_mandate(self, mandate_data):
        """Create a new payment mandate."""
        return self._post_payment_mandate(mandate_data)

    def update_payment_mandate(self, mandate_id, mandate_data):
        """Update an existing payment mandate."""
        url = f'{self.base_url}/payment_mandates/{mandate_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'payment_mandate': mandate_data})
        if response.status_code == 200:
            return response.json().get('payment_mandate', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WritePaymentMandate(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new payment mandate
    mandate_data = {
        'customer_id': 123456,
        'amount': 100.00,
        'currency': 'USD',
        'mandate_type': 'recurring',
        'status': 'pending'
    }

    created_mandate = writer.create_payment_mandate(mandate_data)
    print('Created Payment Mandate:', created_mandate)

    # Example data to update an existing payment mandate
    mandate_id = created_mandate.get('id')
    updated_mandate_data = {
        'status': 'completed'
        # Add other fields to update as necessary
    }

    updated_mandate = writer.update_payment_mandate(mandate_id, updated_mandate_data)
    print('Updated Payment Mandate:', updated_mandate)
