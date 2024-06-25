import requests

PARAMETERS = {
    'amount': 10,
    'category': 9,  # General knowledge category
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php', params=PARAMETERS)
response.raise_for_status()

data = response.json()
question_data = data['results']
