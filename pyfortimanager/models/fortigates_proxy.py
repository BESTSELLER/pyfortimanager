from pyfortimanager.core.fortimanager import FortiManager


class FortiGates_Proxy(FortiManager):
    """API class for proxy calls to FortiGates. Send and receive API calls to/from an online FortiGate.
    """

    def __init__(self, **kwargs):
        super(FortiGates_Proxy, self).__init__(**kwargs)

    def interfaces(self, fortigate: str, adom: str=None, scope: str="global", include_vlan: bool=True, include_aggregate: bool=True, interface_name: str=None, timeout: int=None):
        """Retrieves a list of interfaces or a specific interface and their configuration on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            include_vlan (str): Enable to include VLANs in result list. Default is True.
            include_aggregate (str): Enable to include Aggregate interfaces in result list. Default is True.
            interface_name (str, optional): Name of a specific interface.
            timeout (int, optional): How long to wait for the FortiGate to respond. Defaults to the proxy_timeout set when the API was instantiated.
            
        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/sys/proxy/json",
            "data":
                {
                    "target": [
                        f"/adom/{adom or self.api.adom}/device/{fortigate}"
                    ],
                    "action": "get",
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": f"/api/v2/monitor/system/interface/select?&scope={scope}&include_vlan={include_vlan}&include_aggregate={include_aggregate}"
                }
        }

        # Optional fields
        if interface_name:
            params['data']['resource'] += f"&interface_name={interface_name}"

        return self.post(method="exec", params=params)