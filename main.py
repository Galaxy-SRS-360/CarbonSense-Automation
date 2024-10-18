import requests

url = 'http://192.168.0.108/mqtt_command_handler.php'  # Make sure the URL includes 'http://'
data = {'command': 'light_one_on'}

response = requests.post(url, data=data)

print(response.text)
