import requests

class WriteReturns:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_return(self, return_data):
        """Send a POST request to create a return."""
        url = f'{self.base_url}/returns.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'return': return_data})
        if response.status_code == 201:
            return response.json().get('return', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_return(self, return_data):
        """Create a new return."""
        return self._post_return(return_data)

    def update_return(self, return_id, return_data):
        """Update an existing return."""
        url = f'{self.base_url}/returns/{return_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'return': return_data})
        if response.status_code == 200:
            return response.json().get('return', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteReturns(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new return
    return_data = {
        'order_id': 1234567890,
        'items': [
            {
                'id': 9876543210,
                'quantity': 1
            }
        ],
        'reason': 'Product damaged',
        'status': 'pending'
        # Add other fields as required by your use case
    }

    created_return = writer.create_return(return_data)
    print('Created Return:', created_return)

    # Example data to update an existing return
    return_id = created_return.get('id')
    updated_return_data = {
        'status': 'completed'
        # Add other fields to update as necessary
    }

    updated_return = writer.update_return(return_id, updated_return_data)
    print('Updated Return:', updated_return)
