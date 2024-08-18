import requests
import pandas as pd

class ReadFulfillments:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_fulfillments_page(self, page=1, limit=250):
        """Retrieve a single page of fulfillments from Shopify."""
        url = f'{self.base_url}/fulfillments.json'
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
            return response.json().get('fulfillments', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_fulfillments(self):
        """Retrieve all fulfillments, handling pagination."""
        all_fulfillments = []
        page = 1
        while True:
            fulfillments = self._get_fulfillments_page(page=page)
            if not fulfillments:
                break
            all_fulfillments.extend(fulfillments)
            page += 1
        return all_fulfillments

    def fulfillments_to_dataframe(self):
        """Convert fulfillments to a pandas DataFrame."""
        fulfillments = self.read_all_fulfillments()
        if fulfillments:
            df = pd.json_normalize(fulfillments)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadFulfillments(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    fulfillments_df = reader.fulfillments_to_dataframe()

    print(fulfillments_df.head())
