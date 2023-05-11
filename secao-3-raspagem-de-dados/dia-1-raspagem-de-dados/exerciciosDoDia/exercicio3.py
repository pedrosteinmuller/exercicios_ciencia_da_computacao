# Faça uma requisição a
# https://scrapethissite.com/pages/advanced/?gotcha=headers
#  e verifique se foi bem sucedida.

import requests

response = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers={"Accept": "text/html", "User-Agent": "mozilla"},
)

assert "bot detected" not in response.text

print(response.text)
