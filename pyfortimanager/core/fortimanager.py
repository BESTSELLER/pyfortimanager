from requests.adapters import HTTPAdapter, Retry
import requests
import atexit


class FortiManager(object):
    """API class for FortiManager login management and post requests.
    """

    def __init__(self, api, **kwargs):
        self.api = api
        self.base_url = f"{self.api.host}/jsonrpc"
        self.max_retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        atexit.register(self.logout)

    def login(self):
        """Logs in to the FortiManager API.

        Returns:
            dict: JSON data.
        """

        # Create a new session
        self.api.session = requests.session()

        data = {
            "method": "exec",
            "params": [
                {
                    "data": {
                        "passwd": self.api.password,
                        "user": self.api.username
                    },
                    "url": "/sys/login/user"
                }
            ],
            "session": self.api.sessionid
        }

        self.api.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
        response = self.api.session.post(url=self.base_url, json=data, verify=self.api.verify)

        # HTTP 200 OK
        if response.status_code == 200:

            # Check if the FortiManager request is successful
            if response.json()['result'][0]['status']['code'] == 0:
                self.api.sessionid = response.json()['session']

            return response.json()

    def logout(self):
        """Logs out of the FortiManager API.

        Returns:
            dict: JSON data.
        """

        # Only try the log out endpoint, if we have a session.
        if self.api.session:
            data = {
                "method": "exec",
                "params": [
                    {
                        "url": "/sys/logout"
                    }
                ],
                "session": self.api.sessionid
            }

            self.api.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
            response = self.api.session.post(url=self.base_url, json=data, verify=self.api.verify)
            
            # HTTP 200 OK
            if response.status_code == 200:
                return response.json()

        # Clear our session variables
        self.api.session = None
        self.api.sessionid = None

    def login_check(self):
        """Checks if we have a valid login session.
        """

        # Check if we have a session
        if self.api.session:
          
            # Use the sys_status endpoint as a test to see if our session is valid in FortiManager
            data = {
                "method": "get",
                "params": [
                    {
                        "url": "/sys/status"
                    }
                ],
                "session": self.api.sessionid
            }

            self.api.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
            sys_status = self.api.session.post(url=self.base_url, json=data, verify=self.api.verify)

            # HTTP 200 OK
            if sys_status.status_code == 200:
              
                # If the FortiManager request is unsuccessful, log in again.
                if sys_status.json()['result'][0]['status']['code'] != 0:
                    self.login()
                  
            # Log in again.
            else:
              self.login()
                  
        # Log in again.
        else:
            self.login()

    def post(self, method: str, params: dict):
        """Sends a POST request to the FortiManager API.

        Args:
            method (str): get, exec, add, set, update, delete.
            params (dict): Payload data to send with the request.

        Returns:
            dict: JSON data.
        """

        self.login_check()

        data = {
            "method": method,
            "params": [params],
            "session": self.api.sessionid
        }

        self.api.session.mount("http://", HTTPAdapter(max_retries=self.max_retries))
        response = self.api.session.post(url=self.base_url, json=data, verify=self.api.verify)

        # HTTP 200 OK
        if response.status_code == 200:
            return response.json()['result'][0]