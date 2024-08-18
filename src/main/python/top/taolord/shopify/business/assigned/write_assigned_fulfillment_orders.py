import requests

class WriteAssignedFulfillmentOrders:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_fulfillment_order(self, fulfillment_order_data):
        """Send a POST request to create a fulfillment order."""
        url = f'{self.base_url}/fulfillment_orders.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'fulfillment_order': fulfillment_order_data})
        if response.status_code == 201:
            return response.json().get('fulfillment_order', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_fulfillment_order(self, fulfillment_order_data):
        """Create a new assigned fulfillment order."""
        return self._post_fulfillment_order(fulfillment_order_data)

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteAssignedFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new fulfillment order
    fulfillment_order_data = {
        'order_id': 123456789,
        'assigned_location_id': 987654321,
        'line_items': [
            {
                'id': 111111111,
                'quantity': 1
            }
        ],
        # Add other required fields here
    }

    created_fulfillment_order = writer.create_fulfillment_order(fulfillment_order_data)

    print(created_fulfillment_order)
