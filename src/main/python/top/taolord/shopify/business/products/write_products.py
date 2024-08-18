import requests

class WriteProducts:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_product(self, product_data):
        """Send a POST request to create a product."""
        url = f'{self.base_url}/products.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'product': product_data})
        if response.status_code == 201:
            return response.json().get('product', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_product(self, product_data):
        """Create a new product."""
        return self._post_product(product_data)

    def update_product(self, product_id, product_data):
        """Update an existing product."""
        url = f'{self.base_url}/products/{product_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'product': product_data})
        if response.status_code == 200:
            return response.json().get('product', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteProducts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new product
    product_data = {
        'title': 'New Product',
        'body_html': '<strong>Good product!</strong>',
        'vendor': 'Vendor Name',
        'product_type': 'Type',
        'variants': [
            {
                'option1': 'Default Title',
                'price': '19.99',
                'sku': '12345'
            }
        ]
    }

    created_product = writer.create_product(product_data)
    print('Created Product:', created_product)

    # Example data to update an existing product
    product_id = created_product.get('id')
    updated_product_data = {
        'title': 'Updated Product Title'
        # Add other fields to update as necessary
    }

    updated_product = writer.update_product(product_id, updated_product_data)
    print('Updated Product:', updated_product)
