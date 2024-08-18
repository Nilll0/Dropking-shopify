import requests
import pandas as pd

class ReadShipping:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_shipping_page(self, page=1, limit=250):
        """Retrieve a single page of shipping data from Shopify."""
        url = f'{self.base_url}/shipping.json'
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
            return response.json().get('shipping', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_shipping(self):
        """Retrieve all shipping data, handling pagination."""
        all_shipping = []
        page = 1
        while True:
            shipping = self._get_shipping_page(page=page)
            if not shipping:
                break
            all_shipping.extend(shipping)
            page += 1
        return all_shipping

    def shipping_to_dataframe(self):
        """Convert shipping data to a pandas DataFrame."""
        shipping = self.read_all_shipping()
        if shipping:
            df = pd.json_normalize(shipping)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadShipping(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    shipping_df = reader.shipping_to_dataframe()

    print(shipping_df.head())
