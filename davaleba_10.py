import requests


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"გამარჯობა მომხმარებელო, {url}-თან დაკავშირება ვერ მოხერხდა"


api_1 = get_data("https://api.github.com/")
api_2 = get_data("https://www.data.com/")
print(api_1)
print("\n \n", api_2)
