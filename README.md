# pyfortimanager
Python API client library for Fortinet's [FortiManager](https://www.fortinet.com/products/management/fortimanager).
It does not provide all endpoints available, but we strongly encourage to make a pull request with missing endpoints.

> **Note:** This library has been built and tested for FortiManager v7.0.x.

## Installation

To install run `pip install pyfortimanager`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start

To begin, import pyfortimanager and instantiate the API.

We need to provide the hostname to the FortiManager instance, a username and password for the API user.
Optional settings are `adom` which defaults to `root` and `verify` which defaults to `True`.


```
import pyfortimanager

FortiManager = pyfortimanager.api(
    host = "https://fmg.fortinet.com",
    username = "username",
    password = "password",
)
```


## Queries

List all FortiGates.
```
fmg_fortigates = FortiManager.FortiGates.all()

for fmg_fortigate in fmg_fortigates['data']:
    print(fmg_fortigate['name'])

>>> FortiGate-VM64-1
>>> FortiGate-VM64-2
>>> FortiGate-VM64-3
```

Get a specific FortiGate
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