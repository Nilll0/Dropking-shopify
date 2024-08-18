import requests
import pandas as pd

class ReadInventory:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_inventory_levels_page(self, page=1, limit=250):
        """Retrieve a single page of inventory levels from Shopify."""
        url = f'{self.base_url}/inventory_levels.json'
        params = {
            'limit': limit,
            'page': page
        }
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get('inventory_levels', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_inventory(self):
        """Retrieve all inventory levels, handling pagination."""
        all_inventory_levels = []
        page = 1
        while True:
            inventory_levels = self._get_inventory_levels_page(page=page)
            if not inventory_levels:
                break
            all_inventory_levels.extend(inventory_levels)
            page += 1
        return all_inventory_levels

    def inventory_to_dataframe(self):
        """Convert inventory levels to a pandas DataFrame."""
        inventory_levels = self.read_all_inventory()
        if inventory_levels:
            df = pd.json_normalize(inventory_levels)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadInventory(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    inventory_df = reader.inventory_to_dataframe()

    print(inventory_df.head())
