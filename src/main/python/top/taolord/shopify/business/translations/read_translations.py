import requests
import pandas as pd


class ReadTranslations:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_translations(self):
        """Retrieve all translations."""
        url = f'{self.base_url}/translations.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('translations', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_translations(self):
        """Retrieve all translations."""
        return self._get_translations()

    def translations_to_dataframe(self):
        """Convert translations to a pandas DataFrame."""
        translations = self.read_all_translations()
        if translations:
            df = pd.json_normalize(translations)
            return df
        else:
            return pd.DataFrame()


if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadTranslations(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    translations_df = reader.translations_to_dataframe()

    print(translations_df.head())
