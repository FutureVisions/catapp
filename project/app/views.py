from django.shortcuts import render
import json
import requests
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variable from  .env.
# Create your views here.

API_KEY= os.getenv("API_KEY")

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        api_url = 'https://api.api-ninjas.com/v1/cats?name=' + name.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        if response.status_code == requests.codes.ok:
            response_json = response.json()
            print(response.text)
            return render(request, 'index.html', {'response':response_json})

        else:
            print("Error:", response.status_code, response.text)
    return render(request, 'index.html')
