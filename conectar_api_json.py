import requests
import json

url = "http://54.94.218.62:8079/1139/datasnap/rest/TPublicServices/ExportDataset/131_RECEITA.LIST.GRID"

payload = json.dumps({
  "outputFormat": "JSON",
  "parameters": {
    "DT_LANCAMENTO": "2024-01-10",
    "ano": 2024
  }
})
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyOTgzMjY4IiwiaXNzIjoiRmF0b3IiLCJzdWIiOiJNR1BQIC0gVGVyZW5jaW8iLCJpYXQiOjE3MTA3MzA4MDAsIm5iZiI6MTcxMDczMDgwMCwiZGF0YWJhc2VfaWQiOiI1ODMxQzZERDRGOTkxNzAwMUYwMUE0NEVEQjA0RDZDOSIsImJhc2VfdXJsIjoiaHR0cDpcL1wvNTQuOTQuMjE4LjYyOjgwNzlcLzExMzlcLyJ9.TGIyaDllogN_kQRayEYn0YhLQnsYtIAkk5rm34vwrTM'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)