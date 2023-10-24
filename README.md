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

### List all FortiGates.
```
fmg_fortigates = FortiManager.FortiGates.all()

for fmg_fortigate in fmg_fortigates['data']:
    print(fmg_fortigate['name'])

>>> FortiGate-VM64-1
>>> FortiGate-VM64-2
>>> FortiGate-VM64-3
```

### Retrieve a specific FortiGate
```
fmg_fortigates = FortiManager.FortiGates.all(fortigate="FortiGate-VM64-1")
```

You can use the status object to check if the request is a success or not, and retrieve the error message.
```
fmg_fortigate = FortiManager.FortiGates.all(fortigate="FortiGate-VM64-4")

if fmg_fortigate['status']['code'] == 0:
    print(fmg_fortigate['data']['name'])
else:
    print(fmg_fortigate['status']['message'])

>>>Object does not exist
```