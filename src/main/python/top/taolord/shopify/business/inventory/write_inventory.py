import requests

class WriteInventory:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_inventory_level(self, inventory_level_data):
        """Send a POST request to create or update an inventory level."""
        url = f'{self.base_url}/inventory_levels.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'inventory_level': inventory_level_data})
        if response.status_code == 201:
            return response.json().get('inventory_level', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_inventory_level(self, inventory_level_data):
        """Create a new inventory level."""
        return self._post_inventory_level(inventory_level_data)

    def update_inventory_level(self, inventory_level_id, inventory_level_data):
        """Update an existing inventory level."""
        url = f'{self.base_url}/inventory_levels/{inventory_level_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'inventory_level': inventory_level_data})
        if response.status_code == 200:
            return response.json().get('inventory_level', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteInventory(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new inventory level
    inventory_level_data = {
        'location_id': 987654321,
        'inventory_item_id': 123456789,
        'available': 100
        # Add other required fields here
    }

    created_inventory_level = writer.create_inventory_level(inventory_level_data)
    print('Created Inventory Level:', created_inventory_level)

    # Example data to update an existing inventory level
    inventory_level_id = created_inventory_level.get('id')
    updated_inventory_level_data = {
        'available': 150
        # Add other fields to update as necessary
    }

    updated_inventory_level = writer.update_inventory_level(inventory_level_id, updated_inventory_level_data)
    print('Updated Inventory Level:', updated_inventory_level)
