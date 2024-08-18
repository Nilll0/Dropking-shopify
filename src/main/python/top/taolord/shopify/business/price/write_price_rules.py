import requests

class WritePriceRules:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_price_rule(self, price_rule_data):
        """Send a POST request to create a price rule."""
        url = f'{self.base_url}/price_rules.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'price_rule': price_rule_data})
        if response.status_code == 201:
            return response.json().get('price_rule', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_price_rule(self, price_rule_data):
        """Create a new price rule."""
        return self._post_price_rule(price_rule_data)

    def update_price_rule(self, price_rule_id, price_rule_data):
        """Update an existing price rule."""
        url = f'{self.base_url}/price_rules/{price_rule_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'price_rule': price_rule_data})
        if response.status_code == 200:
            return response.json().get('price_rule', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WritePriceRules(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new price rule
    price_rule_data = {
        'title': 'Summer Sale',
        'target_type': 'line_item',
        'target_selection': 'all',
        'allocation_method': 'across',
        'value_type': 'percentage',
        'value': -20.0,
        'customer_selection': 'all',
        'starts_at': '2024-08-01T00:00:00Z',
        'ends_at': '2024-08-31T23:59:59Z'
    }

    created_price_rule = writer.create_price_rule(price_rule_data)
    print('Created Price Rule:', created_price_rule)

    # Example data to update an existing price rule
    price_rule_id = created_price_rule.get('id')
    updated_price_rule_data = {
        'title': 'Updated Summer Sale',
        'value': -25.0  # Change discount to 25%
    }

    updated_price_rule = writer.update_price_rule(price_rule_id, updated_price_rule_data)
    print('Updated Price Rule:', updated_price_rule)
