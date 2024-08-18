import requests

class WriteLocales:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_locale(self, locale_data):
        """Send a POST request to create or update a locale."""
        url = f'{self.base_url}/locales.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'locale': locale_data})
        if response.status_code == 201:
            return response.json().get('locale', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_locale(self, locale_data):
        """Create a new locale."""
        return self._post_locale(locale_data)

    def update_locale(self, locale_id, locale_data):
        """Update an existing locale."""
        url = f'{self.base_url}/locales/{locale_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'locale': locale_data})
        if response.status_code == 200:
            return response.json().get('locale', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteLocales(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new locale
    locale_data = {
        'locale': 'en',
        'name': 'English',
        'translations': {
            'hello': 'Hello'
            # Add other translation key-value pairs as necessary
        }
    }

    created_locale = writer.create_locale(locale_data)
    print('Created Locale:', created_locale)

    # Example data to update an existing locale
    locale_id = created_locale.get('id')
    updated_locale_data = {
        'name': 'British English'
        # Add other fields to update as necessary
    }

    updated_locale = writer.update_locale(locale_id, updated_locale_data)
    print('Updated Locale:', updated_locale)
