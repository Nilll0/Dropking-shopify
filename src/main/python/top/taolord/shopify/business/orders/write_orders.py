import requests

class WriteOrders:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_order(self, order_data):
        """Send a POST request to create an order."""
        url = f'{self.base_url}/orders.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'order': order_data})
        if response.status_code == 201:
            return response.json().get('order', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_order(self, order_data):
        """Create a new order."""
        return self._post_order(order_data)

    def update_order(self, order_id, order_data):
        """Update an existing order."""
        url = f'{self.base_url}/orders/{order_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'order': order_data})
        if response.status_code == 200:
            return response.json().get('order', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new order
    order_data = {
        'line_items': [
            {
                'variant_id': 123456789,
                'quantity': 1
            }
        ],
        'customer': {
            'id': 987654321
        },
        'billing_address': {
            'address1': '123 Shopify St',
            'city': 'Shopifyville',
            'province': 'ON',
            'country': 'CA',
            'zip': 'A1B 2C3',
            'phone': '123-456-7890'
        },
        'shipping_address': {
            'address1': '123 Shopify St',
            'city': 'Shopifyville',
            'province': 'ON',
            'country': 'CA',
            'zip': 'A1B 2C3',
            'phone': '123-456-7890'
        },
        'email': 'customer@example.com'
    }

    created_order = writer.create_order(order_data)
    print('Created Order:', created_order)

    # Example data to update an existing order
    order_id = created_order.get('id')
    updated_order_data = {
        'note': 'Updated note for the order'
        # Add other fields to update as necessary
    }

    updated_order = writer.update_order(order_id, updated_order_data)
    print('Updated Order:', updated_order)
