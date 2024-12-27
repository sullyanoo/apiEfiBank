import requests
import base64
import json
import os
from functools import partial
from Routes.endpoints import Constants  # Assuming Constants class is in constants.py

class Endpoints:
    def __init__(self, options):
        self.token = None
        self.options = options
        self.base_url = ""
        self.endpoints = {}
        self.urls = {}
        self.cert = False

        # API type (e.g., 'CHARGES', 'PIX', 'OPEN-FINANCE', 'PAYMENTS')
        self.api_type = options.get('api_type', 'CHARGES')  # Default is 'CHARGES'
        self.set_endpoints()

    def set_endpoints(self):
        """
        Set the endpoints for the selected API type (CHARGES, PIX, OPEN-FINANCE, PAYMENTS, etc.)
        """
        if self.api_type not in Constants.APIS:
            raise ValueError(f"API type {self.api_type} not found in Constants.")
        
        self.endpoints = Constants.APIS[self.api_type]['ENDPOINTS']
        self.urls = Constants.APIS[self.api_type]['URL']

    def __getattr__(self, name):
        # If the endpoint exists in the selected API type, return the corresponding method
        if name in self.endpoints:
            self.get_base_url()
            return partial(self.request, self.endpoints[name])
        
        raise AttributeError(f"Endpoint {name} not found for API type {self.api_type}.")

    def request(self, settings, **kwargs):
        if not self.base_url:
            raise Exception("Base URL not configured.")
        
        oauth = self.authenticate()
        if oauth != 200:
            raise Exception("Authentication failed.")
        
        params = kwargs.get("params", {})
        body = kwargs.get("body", {})
        headers = kwargs.get("headers", {})

        # Send the request and return the response
        response = self.send(settings, params, body, headers)
        
        try:
            return response.json()
        except json.JSONDecodeError:
            raise Exception(f"Error decoding JSON response. Status: {response.status_code}, Response: {response.text}")

    def send(self, settings, params, body, headers_complement):
        url = self.build_url(settings["route"], params)
        headers = {
            "Authorization": f"Bearer {self.token['access_token']}",
            "Content-Type": "application/json",
        }
        headers.update(headers_complement)

        if self.cert:
            cert = self.options["certificate"]
            if os.path.exists(cert):
                return requests.request(
                    settings["method"], url, headers=headers, data=json.dumps(body), cert=cert
                )
            else:
                raise FileNotFoundError(f"Certificate not found: {cert}")
        else:
            return requests.request(settings["method"], url, json=body, headers=headers)

    def authenticate(self):
        # Authenticate and return the authentication status
        url = self.build_url("/oauth/token", {})
        auth = base64.b64encode(
            f"{self.options['client_id']}:{self.options['client_secret']}".encode()
        ).decode()
        payload = {"grant_type": "client_credentials"}
        headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

        cert = self.options["certificate"]
        if os.path.exists(cert):
            response = requests.post(url, headers=headers, json=payload, cert=cert)
        else:
            raise FileNotFoundError(f"Certificate not found: {cert}")

        if response.status_code == 200:
            self.token = response.json()
        return response.status_code

    def get_base_url(self):
        # Return the base URL depending on whether we're in sandbox or production
        self.base_url = self.urls['sandbox'] if self.options.get("sandbox") else self.urls['production']

    def build_url(self, route, params):
        # Build the final URL based on the route and provided parameters
        url = f"{self.base_url}{route}"
        if params:
            url += "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        return url

    def refresh_token(self):
        # Method to refresh the token (if the API supports it)
        url = self.build_url("/oauth/token", {})
        auth = base64.b64encode(
            f"{self.options['client_id']}:{self.options['client_secret']}".encode()
        ).decode()
        payload = {"grant_type": "refresh_token", "refresh_token": self.token["refresh_token"]}
        headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

        cert = self.options["certificate"]
        if os.path.exists(cert):
            response = requests.post(url, headers=headers, json=payload, cert=cert)
        else:
            raise FileNotFoundError(f"Certificate not found: {cert}")

        if response.status_code == 200:
            self.token = response.json()
        return response.status_code
