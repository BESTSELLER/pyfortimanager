from pyfortimanager.core.fortimanager import FortiManager


class Policy_Packages(FortiManager):
    """API class for Policy Packages in Policy & Objects.
    """

    def __init__(self, **kwargs):
        super(Policy_Packages, self).__init__(**kwargs)

    def all(self, name: str = None, adom: str = None):
        """Retrieves all policy packages or a single policy package with members.

        Args:
            name (str, optional): Name of a policy package.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}"
        }

        # Retrieve a single policy package
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add(self, name: str, ngfw_mode: int = 0, central_nat: int = 0, policy_offload_level: int = 0, subfolder: str = None, adom: str = None):
        """Adds a new policy package.

        Args:
            name (str): Name of the policy package.
            ngfw_mode (int): 0 = Profile-based.  1 = Policy-based. Default is 0.
            central_nat (int): Enable or disable Central NAT. Default is 0 (disabled).
            policy_offload_level (int): 0 = Disable. 1 = Default. 2 = DoS Offload. 3 = Full Offload. Default is 0.
            subfolder (str, optional): Place the new policy package in a specific folder.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        if subfolder:
            params = {
                "url": f"/pm/pkg/adom/{adom or self.api.adom}",
                "data": [
                    {
                        "name": subfolder,
                        "type": "folder",
                        "subobj": [
                            {
                                "name": name,
                                "type": "pkg",
                                "package settings": {
                                    "ngfw-mode": ngfw_mode,
                                    "central-nat": central_nat,
                                    "policy-offload-level": policy_offload_level
                                }
                            }
                        ]
                    }
                ]
            }
        else:
            params = {
                "url": f"/pm/pkg/adom/{adom or self.api.adom}",
                "data": [
                    {
                        "name": name,
                        "type": "pkg",
                        "package settings": {
                            "ngfw-mode": ngfw_mode,
                            "central-nat": central_nat,
                            "policy-offload-level": policy_offload_level
                        }
                    }
                ]
            }

        return self.post(method="set", params=params)

    def update(self, name: str, ngfw_mode: int, central_nat: int, policy_offload_level: int, rename: str = None, adom: str = None):
        """Updates a policy package.

        Args:
            name (str): Name of the policy package to update.
            rename (str, optional): New name of the policy package.
            ngfw_mode (int): 0 = Profile-based.  1 = Policy-based.
            central_nat (int): Enable or disable Central NAT.
            policy_offload_level (int): 0 = Disable. 1 = Default. 2 = DoS Offload. 3 = Full Offload.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}",
            "data": {
                "name": rename or name,
                "package settings": {
                    "ngfw-mode": ngfw_mode,
                    "central-nat": central_nat,
                    "policy-offload-level": policy_offload_level
                }
            }
        }

        return self.post(method="update", params=params)

    def delete(self, name: str, adom: str = None):
        """Delete a policy package or folder.

        Args:
            name (str): Name of the policy package or folder to delete. Use the full path for the policy package.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}"
        }

        return self.post(method="delete", params=params)

    def clone(self, clone: str, name: str, subfolder: str = None, adom: str = None):
        """Clones a policy package.

        Args:
            clone (str): Name of the policy package to clone.
            name (str): Name for the cloned policy package.
            subfolder (str, optional): Subfolder path for the cloned policy package.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/securityconsole/package/clone",
            "data": {
                "adom": adom or self.api.adom,
                "dst_name": name,
                "pkg": clone
            }
        }

        # Optional fields
        if subfolder:
            params['data']['dst_parent'] = subfolder

        return self.post(method="exec", params=params)

    def move(self, name: str, rename: str = None, folder: str = None, adom: str = None):
        """Moves a policy package to another folder.

        Args:
            name (str): Name for the policy package to move.
            renme (str, optional): Rename the policy package.
            folder (str): New destination folder path for the policy package.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/securityconsole/package/move",
            "data": {
                "adom": adom or self.api.adom,
                "pkg": name,
                "dst_name": rename or name,
                "dst_parent": folder,
            }
        }

        return self.post(method="exec", params=params)

    def add_folder(self, name: str, policy_offload_level: int = 0, subfolder: str = None, adom: str = None):
        """Adds a new folder.

        Args:
            name (str): Name of the new folder.
            policy_offload_level (int): 0 = Disable. 1 = Default. 2 = DoS Offload. 3 = Full Offload. Default is 0.
            subfolder (str, optional): Place the new folder in a specific subfolder.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        if subfolder:
            params = {
                "url": f"/pm/pkg/adom/{adom or self.api.adom}",
                "data": [
                    {
                        "name": subfolder,
                        "type": "folder",
                        "subobj": [
                            {
                                "name": name,
                                "type": "folder",
                                "package settings": {
                                    "policy-offload-level": policy_offload_level
                                }
                            }
                        ]
                    }
                ]
            }
        else:
            params = {
                "url": f"/pm/pkg/adom/{adom or self.api.adom}",
                "data": [
                    {
                        "name": name,
                        "type": "folder",
                        "package settings": {
                            "policy-offload-level": policy_offload_level
                        }
                    }
                ]
            }

        return self.post(method="set", params=params)

    def update_folder(self, name: str, policy_offload_level: int, rename: str = None, adom: str = None):
        """Updates a folder.

        Args:
            name (str): Name of the folder to update.
            rename (str, optional): New name of the folder.
            policy_offload_level (int): 0 = Disable. 1 = Default. 2 = DoS Offload. 3 = Full Offload.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}",
            "data": {
                "name": rename or name,
                "package settings": {
                    "policy-offload-level": policy_offload_level
                }
            }
        }

        return self.post(method="update", params=params)

    def add_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Adds a FortiGate as a member to a policy package.

        Args:
            name (str): Name of the policy package.
            fortigate (str): Name of the FortiGate to be added as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="add", params=params)

    def remove_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Removes a FortiGate as a member from a policy package.

        Args:
            name (str): Name of the policy package.
            fortigate (str): Name of the FortiGate to remove as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="delete", params=params)

    def firewall_policies(self, name: str, adom: str = None):
        """Retrieves all firewall policies in a policy package.

        Args:
            name (str): Name of the policy package.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/pkg/{name}/firewall/policy",
        }

        return self.post(method="get", params=params)
