import requests
import pandas as pd

class ReadPurchaseOptions:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_purchase_options_page(self, page=1, limit=250):
        """Retrieve a single page of purchase options from Shopify."""
        url = f'{self.base_url}/purchase_options.json'
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
            return response.json().get('purchase_options', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_purchase_options(self):
        """Retrieve all purchase options, handling pagination."""
        all_purchase_options = []
        page = 1
        while True:
            purchase_options = self._get_purchase_options_page(page=page)
            if not purchase_options:
                break
            all_purchase_options.extend(purchase_options)
            page += 1
        return all_purchase_options

    def purchase_options_to_dataframe(self):
        """Convert purchase options to a pandas DataFrame."""
        purchase_options = self.read_all_purchase_options()
        if purchase_options:
            df = pd.json_normalize(purchase_options)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadPurchaseOptions(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    purchase_options_df = reader.purchase_options_to_dataframe()

    print(purchase_options_df.head())
