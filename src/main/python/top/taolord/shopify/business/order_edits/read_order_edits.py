import requests
import pandas as pd

class ReadOrderEdits:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_order_edits(self, page=1, limit=250):
        """Retrieve a single page of order edits."""
        url = f'{self.base_url}/order_edits.json'
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
            return response.json().get('order_edits', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_order_edits(self):
        """Retrieve all order edits, handling pagination."""
        all_edits = []
        page = 1
        while True:
            edits = self._get_order_edits(page=page)
            if not edits:
                break
            all_edits.extend(edits)
            page += 1
        return all_edits

    def order_edits_to_dataframe(self):
        """Convert order edits to a pandas DataFrame."""
        edits = self.read_all_order_edits()
        if edits:
            df = pd.json_normalize(edits)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadOrderEdits(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    order_edits_df = reader.order_edits_to_dataframe()

    print(order_edits_df.head())
