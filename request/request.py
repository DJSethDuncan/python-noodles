import requests

if __name__ == '__main__':
    response = requests.get('http://www.google.com')
    print(f"Response: {response.content}")
