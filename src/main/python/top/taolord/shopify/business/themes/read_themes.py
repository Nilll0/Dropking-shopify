import requests
import pandas as pd

class ReadThemes:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_themes(self):
        """Retrieve all themes."""
        url = f'{self.base_url}/themes.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('themes', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_themes(self):
        """Retrieve all themes."""
        return self._get_themes()

    def themes_to_dataframe(self):
        """Convert themes to a pandas DataFrame."""
        themes = self.read_all_themes()
        if themes:
            df = pd.json_normalize(themes)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadThemes(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    themes_df = reader.themes_to_dataframe()

    print(themes_df.head())
