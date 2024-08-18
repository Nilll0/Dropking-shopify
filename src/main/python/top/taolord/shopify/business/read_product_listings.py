import requests
import pandas as pd

class ReadProductListings:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_product_listings_page(self, page=1, limit=250):
        """Retrieve a single page of product listings from Shopify."""
        url = f'{self.base_url}/product_listings.json'
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
            return response.json().get('product_listings', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_product_listings(self):
        """Retrieve all product listings, handling pagination."""
        all_product_listings = []
        page = 1
        while True:
            product_listings = self._get_product_listings_page(page=page)
            if not product_listings:
                break
            all_product_listings.extend(product_listings)
            page += 1
        return all_product_listings

    def product_listings_to_dataframe(self):
        """Convert product listings to a pandas DataFrame."""
        product_listings = self.read_all_product_listings()
        if product_listings:
            df = pd.json_normalize(product_listings)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadProductListings(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    product_listings_df = reader.product_listings_to_dataframe()

    print(product_listings_df.head())
