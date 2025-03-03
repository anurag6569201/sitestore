from django.shortcuts import render

# Create your views here.
import whois
from itertools import product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import whois

@csrf_exempt
def website_details(request):
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = JsonResponse({'detail': 'OPTIONS method allowed.'})
        response['Allow'] = 'POST, OPTIONS'
        return response

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            domain = data.get('website')
            if not domain:
                return JsonResponse({'error': 'No domain provided.'}, status=400)
            
            # Check domain availability
            try:
                domain_info = whois.whois(domain)
                is_available = not domain_info.status
                print(domain_info)
            except Exception:
                is_available = True
            
            return JsonResponse(domain_info)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from bs4 import BeautifulSoup

@csrf_exempt
def get_about(request):
    print("came here...")

    if request.method == 'OPTIONS':
        response = JsonResponse({'detail': 'OPTIONS method allowed.'})
        response['Allow'] = 'POST, OPTIONS'
        return response

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            domain = data.get('website')
            if not domain:
                return JsonResponse({'error': 'No domain provided.'}, status=400)

            try:
                # Send a GET request to the website
                response = requests.get(domain, timeout=10)  # Set a timeout to prevent long waits
                response.raise_for_status()  # Raise an error for HTTP errors (e.g., 404, 500)

                # Parse the HTML content of the website using BeautifulSoup
                soup = BeautifulSoup(response.text, 'lxml')

                # Try to get the meta description
                meta_description = soup.find('meta', attrs={'name': 'description'})
                description = meta_description.get('content', 'Description not available.') if meta_description else None

                # Check for alternative ways to describe the site (h1, h2, p, etc.)
                if not description:
                    description_fallback = soup.find_all(['h1', 'h2', 'p', 'section', 'article'])
                    description_text = "\n".join(
                        [tag.get_text(strip=True) for tag in description_fallback if tag.get_text(strip=True)]
                    )
                    description = description_text if description_text else "Could not find a description on the website."

                return JsonResponse({'description': description})  # Return the data in a dictionary format

            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

@csrf_exempt
def capture_screenshot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            url = data.get('website')
            if not url:
                return JsonResponse({'error': 'No URL provided.'}, status=400)

            # Set up Edge options to run in headless mode
            edge_options = Options()
            edge_options.add_argument('--headless')  # Run in headless mode
            edge_options.add_argument('--disable-gpu')  # Disable GPU for headless mode
            edge_options.add_argument('--no-sandbox')  # Disable sandboxing

            # Set path to Edge WebDriver (msedgedriver)
            driver_path = "C:\\edgedriver_win64\\msedgedriver.exe"  # Adjust this path

            # Initialize the WebDriver
            service = Service(driver_path)
            driver = webdriver.Edge(service=service, options=edge_options)

            screenshot_path = "screenshot.png"

            try:
                # Open the website URL
                driver.get(url)
                time.sleep(3)  # Wait for the page to load

                # Take a screenshot and save it
                driver.save_screenshot(screenshot_path)

                # Close the driver
                driver.quit()

                # Return the image as a response
                return FileResponse(open(screenshot_path, 'rb'), content_type='image/png')

            except Exception as e:
                driver.quit()
                return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def all(url):
    pass