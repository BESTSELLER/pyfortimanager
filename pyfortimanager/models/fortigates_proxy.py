from pyfortimanager.core.fortimanager import FortiManager


class FortiGates_Proxy(FortiManager):
    """API class for proxy calls to FortiGates. Send and receive API calls to/from an online FortiGate.
    """

    def __init__(self, **kwargs):
        super(FortiGates_Proxy, self).__init__(**kwargs)

    def status(self, fortigate: str, adom: str = None, timeout: int = None):
        """Retrieve basic system status on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
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
                    "resource": f"/api/v2/monitor/system/status"
                }
        }

        return self.post(method="exec", params=params)

    def resource_usage(self, fortigate: str, adom: str = None, scope: str = "global", resource: str = None, interval: str = None, timeout: int = None):
        """Retrieves current and historical usage data for a provided resource on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            resource (str. optional): Get a specific resource to get usage data for. Defaults to all resources. 
            interval (str, optional): Time interval of resource usage [1-min|10-min|30-min|1-hour|12-hour|24-hour]. Defaults to all intervals.
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
                    "resource": f"/api/v2/monitor/system/resource/usage/?scope={scope}"
                }
        }

        # Optional fields
        if resource:
            params['data']['resource'] += f"&resource={resource}"

        if interval:
            params['data']['resource'] += f"&interval={interval}"

        return self.post(method="exec", params=params)

    def interfaces(self, fortigate: str, adom: str = None, scope: str = "global", include_vlan: bool = True, include_aggregate: bool = True, interface: str = None, timeout: int = None):
        """Retrieves a list of interfaces or a specific interface and their configuration on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            include_vlan (bool): Enable to include VLANs in result list. Default is True.
            include_aggregate (bool): Enable to include Aggregate interfaces in result list. Default is True.
            interface (str, optional): Retrieve this interface only.
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
                    "resource": f"/api/v2/monitor/system/interface/?scope={scope}&include_vlan={include_vlan}&include_aggregate={include_aggregate}"
                }
        }

        # Optional fields
        if interface:
            params['data']['resource'] += f"&interface_name={interface}"

        return self.post(method="exec", params=params)

    def transceivers(self, fortigate: str, adom: str = None, scope: str = "global", timeout: int = None):
        """Retrieves a list of transceivers used on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
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
                    "resource": f"/api/v2/monitor/system/interface/transceivers?scope={scope}"
                }
        }

        return self.post(method="exec", params=params)

    def dhcp_leases(self, fortigate: str, adom: str = None, scope: str = "global", ipv6: bool = True, interface: str = None, timeout: int = None):
        """Retrieves a list of all DHCP and DHCPv6 leases on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            ipv6 (bool): Include IPv6 addresses in the response. Default is True.
            interface (str, optional): Retrieve DHCP leases for this interface only.
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
                    "resource": f"/api/v2/monitor/system/dhcp/?scope={scope}&ipv6={ipv6}"
                }
        }

        # Optional fields
        if interface:
            params['data']['resource'] += f"&interface={interface}"

        return self.post(method="exec", params=params)
