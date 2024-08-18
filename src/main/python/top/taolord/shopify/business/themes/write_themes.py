import requests

class WriteThemes:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_theme(self, theme_data):
        """Send a POST request to create a theme."""
        url = f'{self.base_url}/themes.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'theme': theme_data})
        if response.status_code == 201:
            return response.json().get('theme', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_theme(self, theme_data):
        """Create a new theme."""
        return self._post_theme(theme_data)

    def update_theme(self, theme_id, theme_data):
        """Update an existing theme."""
        url = f'{self.base_url}/themes/{theme_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'theme': theme_data})
        if response.status_code == 200:
            return response.json().get('theme', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteThemes(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new theme
    theme_data = {
        'name': 'New Theme',
        'role': 'main'
        # Add other fields as required by your use case
    }

    created_theme = writer.create_theme(theme_data)
    print('Created Theme:', created_theme)

    # Example data to update an existing theme
    theme_id = created_theme.get('id')
    updated_theme_data = {
        'name': 'Updated Theme Name'
        # Add other fields to update as necessary
    }

    updated_theme = writer.update_theme(theme_id, updated_theme_data)
    print('Updated Theme:', updated_theme)
