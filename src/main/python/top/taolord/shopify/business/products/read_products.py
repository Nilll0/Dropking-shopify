import requests
import pandas as pd

class ReadProducts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_products_page(self, page=1, limit=250):
        """Retrieve a single page of products from Shopify."""
        url = f'{self.base_url}/products.json'
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
            return response.json().get('products', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_products(self):
        """Retrieve all products, handling pagination."""
        all_products = []
        page = 1
        while True:
            products = self._get_products_page(page=page)
            if not products:
                break
            all_products.extend(products)
            page += 1
        return all_products

    def products_to_dataframe(self):
        """Convert products to a pandas DataFrame."""
        products = self.read_all_products()
        if products:
            df = pd.json_normalize(products)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadProducts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    products_df = reader.products_to_dataframe()

    print(products_df.head())
