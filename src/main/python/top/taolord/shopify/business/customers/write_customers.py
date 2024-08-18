import requests

class WriteCustomers:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_customer(self, customer_data):
        """Send a POST request to create or update a customer."""
        url = f'{self.base_url}/customers.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'customer': customer_data})
        if response.status_code == 201:
            return response.json().get('customer', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_customer(self, customer_data):
        """Create a new customer."""
        return self._post_customer(customer_data)

    def update_customer(self, customer_id, customer_data):
        """Update an existing customer."""
        url = f'{self.base_url}/customers/{customer_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'customer': customer_data})
        if response.status_code == 200:
            return response.json().get('customer', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WriteCustomers(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new customer
    customer_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '+15555555555',
        'addresses': [
            {
                'address1': '123 Example St',
                'city': 'Sample City',
                'province': 'Sample State',
                'country': 'US',
                'zip': '12345'
            }
        ]
        # Add other required fields here
    }

    created_customer = writer.create_customer(customer_data)
    print('Created Customer:', created_customer)

    # Example data to update an existing customer
    customer_id = created_customer.get('id')
    updated_customer_data = {
        'first_name': 'Jane'
        # Add other fields to update as necessary
    }

    updated_customer = writer.update_customer(customer_id, updated_customer_data)
    print('Updated Customer:', updated_customer)
