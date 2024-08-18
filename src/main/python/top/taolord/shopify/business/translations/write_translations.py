import requests


class WriteTranslations:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_translation(self, translation_data):
        """Send a POST request to create a translation."""
        url = f'{self.base_url}/translations.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'translation': translation_data})
        if response.status_code == 201:
            return response.json().get('translation', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_translation(self, translation_data):
        """Create a new translation."""
        return self._post_translation(translation_data)

    def update_translation(self, translation_id, translation_data):
        """Update an existing translation."""
        url = f'{self.base_url}/translations/{translation_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'translation': translation_data})
        if response.status_code == 200:
            return response.json().get('translation', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}


if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteTranslations(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new translation
    translation_data = {
        'key': 'example_key',
        'value': 'Translated text',
        'locale': 'en'
        # Add other fields as required by your use case
    }

    created_translation = writer.create_translation(translation_data)
    print('Created Translation:', created_translation)

    # Example data to update an existing translation
    translation_id = created_translation.get('id')
    updated_translation_data = {
        'value': 'Updated translated text'
        # Add other fields to update as necessary
    }

    updated_translation = writer.update_translation(translation_id, updated_translation_data)
    print('Updated Translation:', updated_translation)
