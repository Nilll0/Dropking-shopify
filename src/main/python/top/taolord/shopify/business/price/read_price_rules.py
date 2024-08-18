import requests
import pandas as pd

class ReadPriceRules:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_price_rules_page(self, page=1, limit=250):
        """Retrieve a single page of price rules from Shopify."""
        url = f'{self.base_url}/price_rules.json'
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
            return response.json().get('price_rules', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_price_rules(self):
        """Retrieve all price rules, handling pagination."""
        all_price_rules = []
        page = 1
        while True:
            price_rules = self._get_price_rules_page(page=page)
            if not price_rules:
                break
            all_price_rules.extend(price_rules)
            page += 1
        return all_price_rules

    def price_rules_to_dataframe(self):
        """Convert price rules to a pandas DataFrame."""
        price_rules = self.read_all_price_rules()
        if price_rules:
            df = pd.json_normalize(price_rules)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadPriceRules(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    price_rules_df = reader.price_rules_to_dataframe()

    print(price_rules_df.head())
