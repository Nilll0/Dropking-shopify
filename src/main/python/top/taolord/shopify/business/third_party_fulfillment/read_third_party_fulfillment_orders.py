import requests
import pandas as pd

class ReadThirdPartyFulfillmentOrders:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_third_party_fulfillment_orders(self, page=1, limit=250):
        """Retrieve a single page of third-party fulfillment orders."""
        url = f'{self.base_url}/third_party_fulfillment_orders.json'
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
            return response.json().get('third_party_fulfillment_orders', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_third_party_fulfillment_orders(self):
        """Retrieve all third-party fulfillment orders, handling pagination."""
        all_orders = []
        page = 1
        while True:
            orders = self._get_third_party_fulfillment_orders(page=page)
            if not orders:
                break
            all_orders.extend(orders)
            page += 1
        return all_orders

    def third_party_fulfillment_orders_to_dataframe(self):
        """Convert third-party fulfillment orders to a pandas DataFrame."""
        orders = self.read_all_third_party_fulfillment_orders()
        if orders:
            df = pd.json_normalize(orders)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadThirdPartyFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    orders_df = reader.third_party_fulfillment_orders_to_dataframe()

    print(orders_df.head())
