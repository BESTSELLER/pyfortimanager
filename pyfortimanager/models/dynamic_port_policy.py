from typing import Optional

from pydantic import Field
from pyfortimanager.core.api import BaseModel, FMGObject, FMGResponse


class DynamicPortPolicy(FMGObject):
    name: str = Field(alias="name")
    vlan_policy: list[str] = Field(default=[], alias="vlan-policy")
    host: Optional[str] = Field(default=None, alias="host")
    mac: Optional[str] = Field(default=None, alias="mac")
    hardware_vendor: Optional[str] = Field(default=None, alias="hw-vendor")
    family: Optional[str] = Field(default=None, alias="family")
    type: Optional[str] = Field(default=None, alias="type")
    bounce_port: bool = Field(default=True, alias="bounce-port-link")
    lldp_profile: list[str] = Field(default=[], alias="lldp-profile")
    qos_policy: list[str] = Field(default=[], alias="qos-policy")
    dot1x_profile: list[str] = Field(default=[], alias="802-1x")


class DynamicPort(FMGObject):
    name: str = Field(alias="name")
    policies: Optional[list[DynamicPortPolicy]] = Field(default=None, alias="policy")


class DynamicPortPolicy(BaseModel):
    """API class for Dynamic Port Policies
    """

    def __init__(self, **kwargs):
        super(DynamicPortPolicy, self).__init__(**kwargs)

    def all(self, fortigate: str, name: Optional[str] = None, fields: Optional[list[str]] = None, vdom: str = "root") -> FMGResponse[DynamicPort]:
        """Retrieves all dynamic port policies or a single dynamic port policy.

        Args:
            fortigate (str): Name of the fortigate to do the update on.
            name (str, optional): Name of a dynamic port policy.
            vdom (str): Name of the VDOM. Defaults to root.

        Returns:
            FMGResponse[DynamicPort]: Parsed response data.
        """

        params = {
            "url": f"pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/dynamic-port-policy",
        }

        if fields:
            params["fields"] = fields

        # Retrieve a single Dynamic Port Policy
        if name:
            params["filter"] += [
                "name",
                "==",
                name
            ],

        return self.post(method="get", params=params, fmg_type=DynamicPort)

    def update(self, fortigate: str, name: str, policies: list[DynamicPortPolicy], vdom: str = "root"):
        """Updates a dynamic port policy

        Args:
            name (str): Name of the dynamic port policy to update.
            fortigate (str): Name of the fortigate to do the update on.
            policies (list[DynamicPort]): The dynamic port policies to update.
            vdom (str): Name of the VDOM. Defaults to root.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/dynamic-port-policy",
			"data": {
				"fortilink": [
					"fortilink"
				],
				"name": name,
				"policy": [
					{
						"status": 1,
						"bounce-port-link": "enable" if policy.bounce_port else "disable",
						"category": "device",
						"name": policy.name,
						"mac": policy.mac,
						"vlan-policy": policy.vlan_policy,
						"host": policy.host,
						"hw-vendor": policy.hardware_vendor,
						"family": policy.family,
						"type": policy.type,
						"lldp-profile": policy.lldp_profile,
						"qos-policy": policy.qos_policy,
						"802-1x": policy.dot1x_profile
					} for policy in policies
				]
			},
            "filter": [
                "name",
                "==",
                name
            ],
        }

        return self.post(method="update", params=params)

