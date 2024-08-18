import requests
import pandas as pd

class ReadLegalPolicies:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _get_legal_policies(self):
        """Retrieve legal policies from Shopify."""
        url = f'{self.base_url}/shop.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            shop_data = response.json().get('shop', {})
            return {
                'refund_policy': shop_data.get('refund_policy', ''),
                'privacy_policy': shop_data.get('privacy_policy', ''),
                'terms_of_service': shop_data.get('terms_of_service', '')
            }
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def read_all_legal_policies(self):
        """Retrieve all legal policies."""
        return self._get_legal_policies()

    def legal_policies_to_dataframe(self):
        """Convert legal policies to a pandas DataFrame."""
        legal_policies = self.read_all_legal_policies()
        if legal_policies:
            df = pd.DataFrame([legal_policies])
            return df
        else:
            return pd.DataFrame()

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    reader = ReadLegalPolicies(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
    legal_policies_df = reader.legal_policies_to_dataframe()

    print(legal_policies_df.head())
