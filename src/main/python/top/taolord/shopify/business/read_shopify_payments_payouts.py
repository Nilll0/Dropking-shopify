import requests
import pandas as pd

class ReadShopifyPaymentsPayouts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_payouts_page(self, page=1, limit=250):
        """Retrieve a single page of Shopify payments payouts."""
        url = f'{self.base_url}/shopify_payments_payouts.json'
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
            return response.json().get('shopify_payments_payouts', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_payouts(self):
        """Retrieve all Shopify payments payouts, handling pagination."""
        all_payouts = []
        page = 1
        while True:
            payouts = self._get_payouts_page(page=page)
            if not payouts:
                break
            all_payouts.extend(payouts)
            page += 1
        return all_payouts

    def payouts_to_dataframe(self):
        """Convert Shopify payments payouts to a pandas DataFrame."""
        payouts = self.read_all_payouts()
        if payouts:
            df = pd.json_normalize(payouts)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadShopifyPaymentsPayouts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    payouts_df = reader.payouts_to_dataframe()

    print(payouts_df.head())
