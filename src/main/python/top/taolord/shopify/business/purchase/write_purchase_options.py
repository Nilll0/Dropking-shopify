import requests

class WritePurchaseOptions:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_purchase_option(self, purchase_option_data):
        """Send a POST request to create a purchase option."""
        url = f'{self.base_url}/purchase_options.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'purchase_option': purchase_option_data})
        if response.status_code == 201:
            return response.json().get('purchase_option', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_purchase_option(self, purchase_option_data):
        """Create a new purchase option."""
        return self._post_purchase_option(purchase_option_data)

    def update_purchase_option(self, purchase_option_id, purchase_option_data):
        """Update an existing purchase option."""
        url = f'{self.base_url}/purchase_options/{purchase_option_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'purchase_option': purchase_option_data})
        if response.status_code == 200:
            return response.json().get('purchase_option', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WritePurchaseOptions(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new purchase option
    purchase_option_data = {
        'title': 'New Purchase Option',
        'description': 'Details about the purchase option',
        'price': '39.99',
        'inventory_quantity': 100
        # Add other fields as required by your use case
    }

    created_purchase_option = writer.create_purchase_option(purchase_option_data)
    print('Created Purchase Option:', created_purchase_option)

    # Example data to update an existing purchase option
    purchase_option_id = created_purchase_option.get('id')
    updated_purchase_option_data = {
        'title': 'Updated Purchase Option Title'
        # Add other fields to update as necessary
    }

    updated_purchase_option = writer.update_purchase_option(purchase_option_id, updated_purchase_option_data)
    print('Updated Purchase Option:', updated_purchase_option)
