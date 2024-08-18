import requests

class WriteThirdPartyFulfillmentOrders:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_third_party_fulfillment_order(self, order_data):
        """Send a POST request to create a third-party fulfillment order."""
        url = f'{self.base_url}/third_party_fulfillment_orders.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'third_party_fulfillment_order': order_data})
        if response.status_code == 201:
            return response.json().get('third_party_fulfillment_order', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_third_party_fulfillment_order(self, order_data):
        """Create a new third-party fulfillment order."""
        return self._post_third_party_fulfillment_order(order_data)

    def update_third_party_fulfillment_order(self, order_id, order_data):
        """Update an existing third-party fulfillment order."""
        url = f'{self.base_url}/third_party_fulfillment_orders/{order_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'third_party_fulfillment_order': order_data})
        if response.status_code == 200:
            return response.json().get('third_party_fulfillment_order', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteThirdPartyFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new third-party fulfillment order
    order_data = {
        'order_id': 1234567890,
        'items': [
            {
                'id': 9876543210,
                'quantity': 1
            }
        ],
        'fulfillment_service': '3rd-party-service',
        'status': 'pending'
        # Add other fields as required by your use case
    }

    created_order = writer.create_third_party_fulfillment_order(order_data)
    print('Created Third-Party Fulfillment Order:', created_order)

    # Example data to update an existing third-party fulfillment order
    order_id = created_order.get('id')
    updated_order_data = {
        'status': 'shipped'
        # Add other fields to update as necessary
    }

    updated_order = writer.update_third_party_fulfillment_order(order_id, updated_order_data)
    print('Updated Third-Party Fulfillment Order:', updated_order)
