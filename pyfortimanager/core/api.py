from pyfortimanager.models.adoms import ADOMs
from pyfortimanager.models.cli_template_groups import CLI_Template_Groups
from pyfortimanager.models.device_groups import Device_Groups
from pyfortimanager.models.fortiaps_proxy import FortiAPs_Proxy
from pyfortimanager.models.fortiaps import FortiAPs
from pyfortimanager.models.fortigates_proxy import FortiGates_Proxy
from pyfortimanager.models.fortigates import FortiGates
from pyfortimanager.models.fortiswitches_proxy import FortiSwitches_Proxy
from pyfortimanager.models.fortiswitches import FortiSwitches
from pyfortimanager.models.install_wizard import Install_Wizard
from pyfortimanager.models.metadata_variables import MetadataVariables
from pyfortimanager.models.policy_packages import Policy_Packages
from pyfortimanager.models.radius_servers import RADIUS_Servers
from pyfortimanager.models.scripts import Scripts
from pyfortimanager.models.sdwan_templates import SDWAN_Templates
from pyfortimanager.models.system import System


class Api(object):
    """Base API class.
    """

    def __init__(self, host: str, token: str, adom: str = "root", verify: bool = True, proxy_timeout: int = 60, **kwargs):
        self.host = host
        self.token = token
        self.adom = adom
        self.verify = verify
        self.proxy_timeout = proxy_timeout

    @property
    def adoms(self):
        """Endpoints related to ADOM management.
        """
        return ADOMs(api=self)

    @property
    def cli_template_groups(self):
        """Endpoints related to CLI Template Groups.
        """
        return CLI_Template_Groups(api=self)

    @property
    def device_groups(self):
        """Endpoints related to Device Groups.
        """
        return Device_Groups(api=self)

    @property
    def fortiaps_proxy(self):
        """Endpoints related to FortiAP proxy calls on a FortiGate.
        """
        return FortiAPs_Proxy(api=self)

    @property
    def fortiaps(self):
        """Endpoints related to FortiAP management.
        """
        return FortiAPs(api=self)

    @property
    def fortigates_proxy(self):
        """Endpoints related to proxy calls on a FortiGate.
        """
        return FortiGates_Proxy(api=self)

    @property
    def fortigates(self):
        """Endpoints related to FortiGate management.
        """
        return FortiGates(api=self)

    @property
    def fortiswitches_proxy(self):
        """Endpoints related to FortiSwitch proxy calls on a FortiGate.
        """
        return FortiSwitches_Proxy(api=self)

    @property
    def fortiswitches(self):
        """Endpoints related to FortiSwitch management.
        """
        return FortiSwitches(api=self)

    @property
    def install_wizard(self):
        """Endpoints related to the Install Wizard.
        """
        return Install_Wizard(api=self)

    @property
    def metadata_variables(self):
        """Endpoints related to Metadata Variables.
        """
        return MetadataVariables(api=self)

    @property
    def policy_packages(self):
        """Endpoints related to Policy Packages.
        """
        return Policy_Packages(api=self)

    @property
    def radius_servers(self):
        """Endpoints related to RADIUS_Servers.
        """
        return RADIUS_Servers(api=self)

    @property
    def scripts(self):
        """Endpoints related to Scripts.
        """
        return Scripts(api=self)

    @property
    def sdwan_templates(self):
        """Endpoints related to SD-WAN Templates.
        """
        return SDWAN_Templates(api=self)

    @property
    def system(self):
        """Endpoints related to the FortiManager system.
        """
        return System(api=self)
