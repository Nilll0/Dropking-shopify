import requests
import pandas as pd

class ReadPaymentMandate:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_payment_mandates_page(self, page=1, limit=250):
        """Retrieve a single page of payment mandates from Shopify."""
        url = f'{self.base_url}/payment_mandates.json'
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
            return response.json().get('payment_mandates', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_payment_mandates(self):
        """Retrieve all payment mandates, handling pagination."""
        all_mandates = []
        page = 1
        while True:
            mandates = self._get_payment_mandates_page(page=page)
            if not mandates:
                break
            all_mandates.extend(mandates)
            page += 1
        return all_mandates

    def payment_mandates_to_dataframe(self):
        """Convert payment mandates to a pandas DataFrame."""
        mandates = self.read_all_payment_mandates()
        if mandates:
            df = pd.json_normalize(mandates)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadPaymentMandate(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    mandates_df = reader.payment_mandates_to_dataframe()

    print(mandates_df.head())
