import requests
import pandas as pd

class ReadReturns:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_returns_page(self, page=1, limit=250):
        """Retrieve a single page of returns."""
        url = f'{self.base_url}/returns.json'
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
            return response.json().get('returns', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_returns(self):
        """Retrieve all returns, handling pagination."""
        all_returns = []
        page = 1
        while True:
            returns = self._get_returns_page(page=page)
            if not returns:
                break
            all_returns.extend(returns)
            page += 1
        return all_returns

    def returns_to_dataframe(self):
        """Convert returns to a pandas DataFrame."""
        returns = self.read_all_returns()
        if returns:
            df = pd.json_normalize(returns)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadReturns(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    returns_df = reader.returns_to_dataframe()

    print(returns_df.head())
