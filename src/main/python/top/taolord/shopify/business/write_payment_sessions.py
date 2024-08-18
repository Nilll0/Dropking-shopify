import requests

class WritePaymentSessions:
    def __init__(self, shop_name, api_version, access_token):
        self.shop_name = shop_name
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = f'https://{shop_name}.myshopify.com/admin/api/{api_version}'

    def _post_payment_session(self, session_data):
        """Send a POST request to create a payment session."""
        url = f'{self.base_url}/payment_sessions.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.post(url, headers=headers, json={'payment_session': session_data})
        if response.status_code == 201:
            return response.json().get('payment_session', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

    def create_payment_session(self, session_data):
        """Create a new payment session."""
        return self._post_payment_session(session_data)

    def update_payment_session(self, session_id, session_data):
        """Update an existing payment session."""
        url = f'{self.base_url}/payment_sessions/{session_id}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        response = requests.put(url, headers=headers, json={'payment_session': session_data})
        if response.status_code == 200:
            return response.json().get('payment_session', {})
        else:
            print(f'Error: {response.status_code}')
            print(response.text)
            return {}

if __name__ == "__main__":
    # Replace these with your actual shop name, API version, and access token
    SHOP_NAME = 'ht-shop-api'
    API_VERSION = '2023-04'
    ACCESS_TOKEN = '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'

    writer = WritePaymentSessions(SHOP_NAME, API_VERSION, ACCESS_TOKEN)

    # Example data to create a new payment session
    session_data = {
        'amount': 100.00,
        'currency': 'USD',
        'payment_method': 'credit_card',
        'status': 'pending'
        # Add other required fields as necessary
    }

    created_session = writer.create_payment_session(session_data)
    print('Created Payment Session:', created_session)

    # Example data to update an existing payment session
    session_id = created_session.get('id')
    updated_session_data = {
        'status': 'completed'
        # Add other fields to update as necessary
    }

    updated_session = writer.update_payment_session(session_id, updated_session_data)
    print('Updated Payment Session:', updated_session)
