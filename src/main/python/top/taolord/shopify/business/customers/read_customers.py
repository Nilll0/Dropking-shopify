import requests
import pandas as pd

class ReadCustomers:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_customers_page(self, page=1, limit=250):
        """Retrieve a single page of customers from Shopify."""
        url = f'{self.base_url}/customers.json'
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
            return response.json().get('customers', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_customers(self):
        """Retrieve all customers, handling pagination."""
        all_customers = []
        page = 1
        while True:
            customers = self._get_customers_page(page=page)
            if not customers:
                break
            all_customers.extend(customers)
            page += 1
        return all_customers

    def customers_to_dataframe(self):
        """Convert customers to a pandas DataFrame."""
        customers = self.read_all_customers()
        if customers:
            df = pd.json_normalize(customers)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadCustomers(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    customers_df = reader.customers_to_dataframe()

    print(customers_df.head())
