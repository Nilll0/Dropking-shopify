import requests

class WriteOwnSubscriptionContracts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_subscription_contract(self, contract_data):
        """Send a POST request to create an own subscription contract."""
        url = f'{self.base_url}/own_subscription_contracts.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'own_subscription_contract': contract_data})
        if response.status_code == 201:
            return response.json().get('own_subscription_contract', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_subscription_contract(self, contract_data):
        """Create a new own subscription contract."""
        return self._post_subscription_contract(contract_data)

    def update_subscription_contract(self, contract_id, contract_data):
        """Update an existing own subscription contract."""
        url = f'{self.base_url}/own_subscription_contracts/{contract_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'own_subscription_contract': contract_data})
        if response.status_code == 200:
            return response.json().get('own_subscription_contract', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteOwnSubscriptionContracts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new subscription contract
    contract_data = {
        'name': 'New Subscription Contract',
        'description': 'Details about the subscription contract',
        'status': 'active'
        # Add other fields as required by your use case
    }

    created_contract = writer.create_subscription_contract(contract_data)
    print('Created Subscription Contract:', created_contract)

    # Example data to update an existing subscription contract
    contract_id = created_contract.get('id')
    updated_contract_data = {
        'name': 'Updated Contract Name'
        # Add other fields to update as necessary
    }

    updated_contract = writer.update_subscription_contract(contract_id, updated_contract_data)
    print('Updated Subscription Contract:', updated_contract)
