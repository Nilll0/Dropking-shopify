import requests
import pandas as pd

class ReadLocales:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_locales_page(self, page=1, limit=250):
        """Retrieve a single page of locales from Shopify."""
        url = f'{self.base_url}/locales.json'
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
            return response.json().get('locales', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_locales(self):
        """Retrieve all locales, handling pagination."""
        all_locales = []
        page = 1
        while True:
            locales = self._get_locales_page(page=page)
            if not locales:
                break
            all_locales.extend(locales)
            page += 1
        return all_locales

    def locales_to_dataframe(self):
        """Convert locales to a pandas DataFrame."""
        locales = self.read_all_locales()
        if locales:
            df = pd.json_normalize(locales)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadLocales(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    locales_df = reader.locales_to_dataframe()

    print(locales_df.head())
