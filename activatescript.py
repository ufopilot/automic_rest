import os
import json
from automic_rest import config
import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




class activateScript:
   def __init__(self, **kwargs):
       # Summary: Runs scripts written in the Automation Engine scripting language.
       self.response = None 
       self.body = None 
       self.url = None 
       self.headers = None 
       self.content = None 
       self.text = None 
       self.status = None 
       self.path = config().setArgs('/{client_id}/scripts', **kwargs)
       self.data = kwargs.get('data',"{}")

       self.request() 

   def request(self): 
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       try: 
            r = requests.post(
                config().url+self.path, 
              headers=headers,
              data=json.dumps(self.data),
                auth=(config().userid, config().password), 
                verify=config().sslverify, 
                timeout=config().timeout 
            ) 
            # request body  
            self.body = r.request.body 
            # request url 
            self.url = r.request.url 
            # response headers 
            self.headers = r.headers 
            # raw bytes 
            self.content = r.content 
            # converts bytes to string 
            self.text = r.text 
            # http status_code 
            self.status = r.status_code 
            # convert raw bytes to json_dict 
            self.response = r.json() 
            # If the response was successful, no Exception will be raised 
            r.raise_for_status() 
       except HTTPError as http_err: 
            print(f'HTTP error occurred: {http_err}')  # Python 3.6 
       except Exception as err: 
            print(f'Other error occurred: {err}')  # Python 3.6 
       except Timeout: 
            print('The request timed out') 
       else: 
            pass 
 
       
       return  self 