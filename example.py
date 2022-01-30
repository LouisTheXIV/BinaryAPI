import requests

word = input("Input Word: ")
print(f'{requests.get(f"https://yourlink/convert={word}").text}')
