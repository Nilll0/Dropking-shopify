import requests
import pandas as pd

class ReadMerchantApprovalSignals:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_merchant_approval_signals_page(self, page=1, limit=250):
        """Retrieve a single page of merchant approval signals from Shopify."""
        url = f'{self.base_url}/merchant_approval_signals.json'
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
            return response.json().get('merchant_approval_signals', [])
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return []

    def read_all_merchant_approval_signals(self):
        """Retrieve all merchant approval signals, handling pagination."""
        all_signals = []
        page = 1
        while True:
            signals = self._get_merchant_approval_signals_page(page=page)
            if not signals:
                break
            all_signals.extend(signals)
            page += 1
        return all_signals

    def merchant_approval_signals_to_dataframe(self):
        """Convert merchant approval signals to a pandas DataFrame."""
        signals = self.read_all_merchant_approval_signals()
        if signals:
            df = pd.json_normalize(signals)
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadMerchantApprovalSignals(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    signals_df = reader.merchant_approval_signals_to_dataframe()

    print(signals_df.head())
