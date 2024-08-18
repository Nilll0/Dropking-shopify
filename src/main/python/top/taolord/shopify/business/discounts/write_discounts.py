import requests

class WriteDiscounts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_discount(self, discount_data):
        """Send a POST request to create or update a discount."""
        url = f'{self.base_url}/discounts.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'discount': discount_data})
        if response.status_code == 201:
            return response.json().get('discount', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_discount(self, discount_data):
        """Create a new discount."""
        return self._post_discount(discount_data)

    def update_discount(self, discount_id, discount_data):
        """Update an existing discount."""
        url = f'{self.base_url}/discounts/{discount_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'discount': discount_data})
        if response.status_code == 200:
            return response.json().get('discount', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteDiscounts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new discount
    discount_data = {
        'discount_code': 'SUMMER20',
        'discount_type': 'percentage',
        'value': '20',
        'starts_at': '2024-08-01T00:00:00Z',
        'ends_at': '2024-08-31T23:59:59Z'
        # Add other required fields here
    }

    created_discount = writer.create_discount(discount_data)
    print('Created Discount:', created_discount)

    # Example data to update an existing discount
    discount_id = created_discount.get('id')
    updated_discount_data = {
        'discount_code': 'SUMMER25'
        # Add other fields to update as necessary
    }

    updated_discount = writer.update_discount(discount_id, updated_discount_data)
    print('Updated Discount:', updated_discount)
