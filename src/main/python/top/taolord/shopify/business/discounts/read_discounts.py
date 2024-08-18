import requests
import pandas as pd

class ReadDiscounts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_discounts_page(self, page=1, limit=250):
        """Retrieve a single page of discounts from Shopify."""
        url = f'{self.base_url}/discounts.json'
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
            return response.json().get('discounts', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_discounts(self):
        """Retrieve all discounts, handling pagination."""
        all_discounts = []
        page = 1
        while True:
            discounts = self._get_discounts_page(page=page)
            if not discounts:
                break
            all_discounts.extend(discounts)
            page += 1
        return all_discounts

    def discounts_to_dataframe(self):
        """Convert discounts to a pandas DataFrame."""
        discounts = self.read_all_discounts()
        if discounts:
            df = pd.json_normalize(discounts)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadDiscounts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    discounts_df = reader.discounts_to_dataframe()

    print(discounts_df.head())
