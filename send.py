import requests


headers = dict()
headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJqdGkiOiJlN2FhOTkyYjEzMjE0NTdiYWVmMTAzZDczMmRlZmI0OSIsInRva2VuX3R5cGUiOiJhY2Nlc3MiLCJleHAiOjE1MjU4NjEyMTN9.F6e_DybomZ2HkKYPu_qyimDIHmtFvl0jw0IUOoRGSHs'

r = requests.get('http://localhost:8000/paradigms/', headers=headers)
print(r.text)
