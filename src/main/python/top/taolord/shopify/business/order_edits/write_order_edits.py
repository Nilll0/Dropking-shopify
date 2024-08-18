import requests

class WriteOrderEdits:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_order_edit(self, edit_data):
        """Send a POST request to create an order edit."""
        url = f'{self.base_url}/order_edits.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'order_edit': edit_data})
        if response.status_code == 201:
            return response.json().get('order_edit', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_order_edit(self, edit_data):
        """Create a new order edit."""
        return self._post_order_edit(edit_data)

    def update_order_edit(self, edit_id, edit_data):
        """Update an existing order edit."""
        url = f'{self.base_url}/order_edits/{edit_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'order_edit': edit_data})
        if response.status_code == 200:
            return response.json().get('order_edit', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteOrderEdits(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new order edit
    edit_data = {
        'order_id': 1234567890,
        'edit': {
            'id': 1,
            'changes': [
                {
                    'property': 'quantity',
                    'old_value': 1,
                    'new_value': 2
                }
            ]
            # Add other fields as required by your use case
        }
    }

    created_edit = writer.create_order_edit(edit_data)
    print('Created Order Edit:', created_edit)

    # Example data to update an existing order edit
    edit_id = created_edit.get('id')
    updated_edit_data = {
        'edit': {
            'changes': [
                {
                    'property': 'quantity',
                    'old_value': 2,
                    'new_value': 3
                }
            ]
            # Add other fields to update as necessary
        }
    }

    updated_edit = writer.update_order_edit(edit_id, updated_edit_data)
    print('Updated Order Edit:', updated_edit)
