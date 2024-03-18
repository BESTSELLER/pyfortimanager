from pyfortimanager.core.fortimanager import FortiManager


class Scripts(FortiManager):
    """API class for Scripts in the Device Manager.
    """

    def __init__(self, **kwargs):
        super(Scripts, self).__init__(**kwargs)

    def all(self, name: str = None, adom: str = None):
        """Retrieves a list of all scripts or a single script.

        Args:
            name (str): Name of a script.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/script"
        }

        # Retrieve a single script
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def execute(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Executes a script on a FortiGate.

        Args:
            name (str): Name of the script to execute.
            fortigate (str): Name of the FortiGate to run the script on.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/script/execute",
            "data": {
                "adom": adom or self.api.adom,
                "script": name,
                "scope": [
                    {
                        "name": fortigate,
                        "vdom": vdom
                    }
                ],
            }
        }

        return self.post(method="exec", params=params)

    def execution_log(self, fortigate: str):
        """Retrieves the script execution log on a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/script/log/list/device/{fortigate}"
        }

        return self.post(method="get", params=params)
