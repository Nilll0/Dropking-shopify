import requests
import pandas as pd

class ReadOwnSubscriptionContracts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_subscription_contracts_page(self, page=1, limit=250):
        """Retrieve a single page of own subscription contracts."""
        url = f'{self.base_url}/own_subscription_contracts.json'
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
            return response.json().get('own_subscription_contracts', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_subscription_contracts(self):
        """Retrieve all own subscription contracts, handling pagination."""
        all_contracts = []
        page = 1
        while True:
            contracts = self._get_subscription_contracts_page(page=page)
            if not contracts:
                break
            all_contracts.extend(contracts)
            page += 1
        return all_contracts

    def subscription_contracts_to_dataframe(self):
        """Convert own subscription contracts to a pandas DataFrame."""
        contracts = self.read_all_subscription_contracts()
        if contracts:
            df = pd.json_normalize(contracts)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadOwnSubscriptionContracts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    contracts_df = reader.subscription_contracts_to_dataframe()

    print(contracts_df.head())
