import requests
import pandas as pd

class ReadUsers:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_users(self, page=1, limit=250):
        """Retrieve a single page of users."""
        url = f'{self.base_url}/users.json'
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
            return response.json().get('users', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_users(self):
        """Retrieve all users, handling pagination."""
        all_users = []
        page = 1
        while True:
            users = self._get_users(page=page)
            if not users:
                break
            all_users.extend(users)
            page += 1
        return all_users

    def users_to_dataframe(self):
        """Convert users to a pandas DataFrame."""
        users = self.read_all_users()
        if users:
            df = pd.json_normalize(users)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadUsers(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    users_df = reader.users_to_dataframe()

    print(users_df.head())
