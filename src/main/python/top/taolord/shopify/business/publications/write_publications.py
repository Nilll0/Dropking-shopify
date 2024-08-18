import requests

class WritePublications:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_publication(self, publication_data):
        """Send a POST request to create a publication."""
        url = f'{self.base_url}/publications.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'publication': publication_data})
        if response.status_code == 201:
            return response.json().get('publication', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_publication(self, publication_data):
        """Create a new publication."""
        return self._post_publication(publication_data)

    def update_publication(self, publication_id, publication_data):
        """Update an existing publication."""
        url = f'{self.base_url}/publications/{publication_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'publication': publication_data})
        if response.status_code == 200:
            return response.json().get('publication', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WritePublications(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new publication
    publication_data = {
        'title': 'New Publication',
        'body_html': '<strong>Exciting news!</strong>',
        'published_at': '2024-08-01T00:00:00Z'
        # Add other fields as required by your use case
    }

    created_publication = writer.create_publication(publication_data)
    print('Created Publication:', created_publication)

    # Example data to update an existing publication
    publication_id = created_publication.get('id')
    updated_publication_data = {
        'title': 'Updated Publication Title'
        # Add other fields to update as necessary
    }

    updated_publication = writer.update_publication(publication_id, updated_publication_data)
    print('Updated Publication:', updated_publication)
