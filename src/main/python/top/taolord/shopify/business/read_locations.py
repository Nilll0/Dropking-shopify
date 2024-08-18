import requests
import pandas as pd

class ReadLocations:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_locations_page(self, page=1, limit=250):
        """Retrieve a single page of locations from Shopify."""
        url = f'{self.base_url}/locations.json'
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
            return response.json().get('locations', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_locations(self):
        """Retrieve all locations, handling pagination."""
        all_locations = []
        page = 1
        while True:
            locations = self._get_locations_page(page=page)
            if not locations:
                break
            all_locations.extend(locations)
            page += 1
        return all_locations

    def locations_to_dataframe(self):
        """Convert locations to a pandas DataFrame."""
        locations = self.read_all_locations()
        if locations:
            df = pd.json_normalize(locations)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadLocations(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    locations_df = reader.locations_to_dataframe()

    print(locations_df.head())
