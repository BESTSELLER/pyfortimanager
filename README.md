# pyfortimanager
Python API client library for Fortinet's [FortiManager](https://www.fortinet.com/products/management/fortimanager).

It does not provide all endpoints or functionality available. We encourage to make a pull request with needed missing endpoints.

> **Note:** This library has been built and tested for FortiManager v7.2.x.

## Installation
To install run `pip install pyfortimanager`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start
To begin, import pyfortimanager and instantiate the API.

We need to provide the IP or FQDN to the FortiManager instance and a user with access to the API.
Optionally, its possible to set `adom` which defaults to `root` and `verify` which defaults to `True`.

**Code**
```
import pyfortimanager
fortimanager = pyfortimanager.api(
    host = "https://fortimanager.example.com",
    token = "<api_token_from_fmg>"
)
```

> **Note:** To generate your API token, check the Fortinet docs [here](https://docs.fortinet.com/document/fortimanager/7.2.0/new-features/47777/fortimanager-supports-authentication-token-for-api-administrators-7-2-2).

## Examples
### List all FortiGates.
There is a ton of data for a single FortiGate. This code retrieves all of it, but only prints the name of the FortiGates.

**Code**
```
fmg_fortigates = fortimanager.fortigates.all()
for fmg_fortigate in fmg_fortigates['data']:
    print(fmg_fortigate['name'])
```

**Output**
```
FortiGate-VM64-1
FortiGate-VM64-2
FortiGate-VM64-3
```

### Status object.
You can use the status object to check if the request is a success or not, and retrieve the error message.

**Code**
```
fmg_fortigate = fortimanager.fortigates.all(fortigate="FortiGate-VM64-4")
if fmg_fortigate['status']['code'] == 0:
    print(fmg_fortigate['data']['name'])
else:
    print(fmg_fortigate['status'])
```

**Output**
```
"status": {
    "code": -3,
    "message": "Object does not exist"
}
```

### Custom API request.
Since FortiManager consists of a ton of API endpoints, not all are supported natively in this module.

You can however use the custom_request function in order to reach any API endpoint in FortiManager.

**Code**
```
fmg_custom_request = fortimanager.system.custom_request(
    params={
        "url": "/dvmdb/adom/root/device",
        "option": [
            "get meta"
        ]
    },
    method="get"
)
print(json.dumps(fmg_custom_request, indent=4))
```

### Adding a FortiGate
This creates a model device in the Device Manager with the minimum required fields.

**Code**
```
fmg_fortigate_add = fortimanager.fortigates.add(
    serial = "FGT60FTK1234ABCD",
    mr = 0,
    os_ver = 7
)
print(fmg_fortigate_add)
```

**Output**
```
{
    "data": {
        "device": {
            "beta": -1,
            "branch_pt": 516,
            "build": 516,
            "conn_mode": 1,
            "dev_status": 1,
            "flags": 67371040,
            "hostname": "FGT60FTK1234ABCD",
            "maxvdom": 10,
            "mgmt_id": 999918516,
            "mgmt_mode": 3,
            "mr": 0,
            "name": "FGT60FTK1234ABCD",
            "oid": 61594,
            "os_type": 0,
            "os_ver": 7,
            "patch": -1,
            "platform_id": 19,
            "platform_str": "FortiGate-60F",
            "sn": "FGT60FTK1234ABCD",
            "source": 1,
            "tab_status": "<unknown>",
            "version": 700
        }
    },
    "status": {
        "code": 0,
        "message": "OK"
    },
    "url": "/dvm/cmd/add/device"
}
```

### Retrieve all connected Wi-Fi clients on a FortiGate
To retrieve all current active Wi-Fi clients on the FortiGate, we need to call the FortiOS API directly on the FortiGate through FortiManager's proxy API.

When making proxy calls, you'll retrieve two status objects. The first is for the FortiManager call and the the second is for the API call on the FortiGate.

> **Note:** Proxy calls only works, if the FortiGate is online.

**Code**
```
fmg_wifi_clients = fortimanager.fortiaps_proxy.clients(fortigate="FortiGate-VM64-1")
print(fmg_wifi_clients)
```

**Output**
```
{
    "data": [
        {
            "response": {
                "action": "",
                "build": 523,
                "http_method": "GET",
                "name": "client",
                "path": "wifi",
                "results": [
                    {
                        "11k_capable": false,
                        "11r_capable": false,
                        "11v_capable": true,
                        "association_time": 1698143761,
                        "authentication": "pass",
                        "bandwidth_rx": 2493967,
                        "bandwidth_tx": 2564936,
                        "captive_portal_authenticated": 0,
                        "channel": 44,
                        "data_rate_bps": 573600000,
                        "data_rxrate_bps": 286800000,
                        "data_txrate_bps": 286800000,
                        "encrypt": 1,
                        "health": {
                            "band": {
                                "severity": "good",
                                "value": "5ghz"
                            },
                            "signal_strength": {
                                "severity": "good",
                                "value": -52
                            },
                            "snr": {
                                "severity": "good",
                                "value": 43
                            },
                            "transmission_discard": {
                                "severity": "good",
                                "value": 0
                            },
                            "transmission_retry": {
                                "severity": "good",
                                "value": 0
                            }
                        },
                        "host": "WINDOWS-PC",
                        "hostname": "WINDOWS-PC",
                        "idle_time": 1,
                        "ip": "10.10.10.10",
                        "ip6": [
                            "fe80::c28d:52e5:68a4:95ad"
                        ],
                        "lan_authenticated": false,
                        "mac": "aa:bb:cc:dd:ee:ff",
                        "manufacturer": "Microsoft",
                        "mimo": "2x2",
                        "noise": -95,
                        "os": "Windows",
                        "radio_type": "802.11ax-5G",
                        "security": 12,
                        "security_str": "wpa2_only_enterprise",
                        "signal": -52,
                        "snr": 43,
                        "ssid": "SSID",
                        "sta_maxrate": 286800,
                        "sta_rxrate": 286800,
                        "sta_rxrate_mcs": 11,
                        "sta_rxrate_score": 100,
                        "sta_txrate": 286800,
                        "sta_txrate_mcs": 11,
                        "sta_txrate_score": 100,
                        "tx_discard_percentage": 0,
                        "tx_retry_percentage": 0,
                        "user": "host/WINDOWS-PC.local.net",
                        "vap_name": "SSID",
                        "vci": "MSFT 5.0",
                        "vlan_id": 101,
                        "wtp_control_ip": "10.20.30.40",
                        "wtp_control_local_ip": "10.20.30.40",
                        "wtp_id": "FP431FTF12345678",
                        "wtp_ip": "10.20.30.40",
                        "wtp_name": "FAP-431F",
                        "wtp_radio": 2
                    }
                ],
                "serial": "FGT60FTK1234ABCD",
                "status": "success",
                "vdom": "root",
                "version": "v7.0.12"
            },
            "status": {
                "code": 0,
                "message": "OK"
            },
            "target": "FortiGate-VM64-1"
        }
    ],
    "status": {
        "code": 0,
        "message": "OK"
    },
    "url": "/sys/proxy/json"
}
```