from pyfortimanager.core.fortimanager import FortiManager


class Install_Wizard(FortiManager):
    """API class for the Install Wizard.
    """

    def __init__(self, **kwargs):
        super(Install_Wizard, self).__init__(**kwargs)

    def device_settings(self, fortigate: str, vdom: str = "root", adom: str = None):
        """Installs the device settings on a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/securityconsole/install/device",
            "data": {
                "adom": adom or self.api.adom,
                "scope": [
                    {
                        "name": fortigate,
                        "vdom": vdom
                    }
                ],
            }
        }

        return self.post(method="exec", params=params)

    def policy_package(self, policy_package: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Installs a policy package on a FortiGate.

        Args:
            policy_package (str): Name of the policy package to be installed.
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/securityconsole/install/package",
            "data": {
                "adom": adom or self.api.adom,
                "flags": "nonblocking",
                "pkg": policy_package,
                "scope": [
                    {
                        "name": fortigate,
                        "vdom": vdom
                    }
                ],
            }
        }

        return self.post(method="exec", params=params)
