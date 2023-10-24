# pyfortimanager
Python API client library for Fortinet's [FortiManager](https://www.fortinet.com/products/management/fortimanager).

It does not provide all endpoints available, but we strongly encourage to make a pull request with missing endpoints.

> **Note:** This library has been built and tested for FortiManager v7.0.x.

## Installation

To install run `pip install pyfortimanager`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start

To begin, import pyfortimanager and instantiate the API.

We need to provide the IP or FQDN to the FortiManager instance and a user with access to the API.

Optionally, its possible to set `adom` which defaults to `root` and `verify` which defaults to `True`.


```
import pyfortimanager

FortiManager = pyfortimanager.api(
    host = "https://fortimanager.example.com",
    username = "apiuser",
    password = "secret",
)
```


## Examples

### List all FortiGates and their configuration (including meta fields).
```
fmg_fortigates = FortiManager.FortiGates.all()

for fmg_fortigate in fmg_fortigates['data']:
    print(fmg_fortigate['name'])
```

**Output**
```
FortiGate-VM64-1
FortiGate-VM64-2
FortiGate-VM64-3
```

### Using the status object.
You can use the status object to check if the request is a success or not, and retrieve the error message.

```
fmg_fortigate = FortiManager.FortiGates.all(fortigate="FortiGate-VM64-4")

if fmg_fortigate['status']['code'] == 0:
    print(fmg_fortigate['data']['name'])
else:
    print(fmg_fortigate['status']['message'])
```

**Output**
```
Object does not exist
```

### Adding a FortiGate
This creates a model device in the Device Manager with the minimum required fields.

```
fmg_fortigate_add = FortiManager.fortigates.add(
    name = "FGT-60F-1",
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
            "name": "FGT-60F-1",
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