import requests
re = requests

ReOb = re.get(url = "https://tylervigen.com/discover")
print(ReOb)
print(ReOb.content)