import requests
import pandas as pd

class ReadShopifyPaymentsDisputes:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_disputes_page(self, page=1, limit=250):
        """Retrieve a single page of Shopify payments disputes."""
        url = f'{self.base_url}/shopify_payments_disputes.json'
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
            return response.json().get('shopify_payments_disputes', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_disputes(self):
        """Retrieve all Shopify payments disputes, handling pagination."""
        all_disputes = []
        page = 1
        while True:
            disputes = self._get_disputes_page(page=page)
            if not disputes:
                break
            all_disputes.extend(disputes)
            page += 1
        return all_disputes

    def disputes_to_dataframe(self):
        """Convert Shopify payments disputes to a pandas DataFrame."""
        disputes = self.read_all_disputes()
        if disputes:
            df = pd.json_normalize(disputes)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadShopifyPaymentsDisputes(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    disputes_df = reader.disputes_to_dataframe()

    print(disputes_df.head())
