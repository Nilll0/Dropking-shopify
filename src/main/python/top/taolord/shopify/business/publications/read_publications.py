import requests
import pandas as pd

class ReadPublications:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_publications_page(self, page=1, limit=250):
        """Retrieve a single page of publications from Shopify."""
        url = f'{self.base_url}/publications.json'
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
            return response.json().get('publications', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_publications(self):
        """Retrieve all publications, handling pagination."""
        all_publications = []
        page = 1
        while True:
            publications = self._get_publications_page(page=page)
            if not publications:
                break
            all_publications.extend(publications)
            page += 1
        return all_publications

    def publications_to_dataframe(self):
        """Convert publications to a pandas DataFrame."""
        publications = self.read_all_publications()
        if publications:
            df = pd.json_normalize(publications)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadPublications(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    publications_df = reader.publications_to_dataframe()

    print(publications_df.head())
