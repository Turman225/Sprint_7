import requests
import helper
URL = 'https://qa-scooter.praktikum-services.ru'

payload = {
    "login": helper.generate_random_string(12),
    "password": helper.generate_random_string(12),
    "firstName": helper.generate_random_string(12)
}

print(payload)
a = requests.post(f'{URL}/api/v1/courier', data=payload)
print(a.status_code)