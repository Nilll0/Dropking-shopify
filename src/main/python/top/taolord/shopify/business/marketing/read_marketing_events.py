import requests
import pandas as pd

class ReadMarketingEvents:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_marketing_events_page(self, page=1, limit=250):
        """Retrieve a single page of marketing events from Shopify."""
        url = f'{self.base_url}/marketing_events.json'
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
            return response.json().get('marketing_events', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_marketing_events(self):
        """Retrieve all marketing events, handling pagination."""
        all_marketing_events = []
        page = 1
        while True:
            marketing_events = self._get_marketing_events_page(page=page)
            if not marketing_events:
                break
            all_marketing_events.extend(marketing_events)
            page += 1
        return all_marketing_events

    def marketing_events_to_dataframe(self):
        """Convert marketing events to a pandas DataFrame."""
        marketing_events = self.read_all_marketing_events()
        if marketing_events:
            df = pd.json_normalize(marketing_events)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadMarketingEvents(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    marketing_events_df = reader.marketing_events_to_dataframe()

    print(marketing_events_df.head())
