import requests
import pandas as pd

class ReadCheckouts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_checkouts_page(self, page=1, limit=250):
        """Retrieve a single page of checkouts from Shopify."""
        url = f'{self.base_url}/checkouts.json'
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
            return response.json().get('checkouts', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_checkouts(self):
        """Retrieve all checkouts, handling pagination."""
        all_checkouts = []
        page = 1
        while True:
            checkouts = self._get_checkouts_page(page=page)
            if not checkouts:
                break
            all_checkouts.extend(checkouts)
            page += 1
        return all_checkouts

    def checkouts_to_dataframe(self):
        """Convert checkouts to a pandas DataFrame."""
        checkouts = self.read_all_checkouts()
        if checkouts:
            df = pd.json_normalize(checkouts)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadCheckouts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    checkouts_df = reader.checkouts_to_dataframe()

    print(checkouts_df.head())
