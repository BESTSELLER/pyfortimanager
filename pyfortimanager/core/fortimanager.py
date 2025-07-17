from pyfortimanager.models.adoms import Adoms
from pyfortimanager.models.cli_template_groups import CLITemplateGroups
from pyfortimanager.models.cli_templates import CLITemplates
from pyfortimanager.models.device_groups import DeviceGroups
from pyfortimanager.models.dynamic_port_policy import DynamicPortPolicy
from pyfortimanager.models.fortiaps_proxy import FortiAPsProxy
from pyfortimanager.models.fortiaps import FortiAPs
from pyfortimanager.models.fortigates_proxy import FortiGatesProxy
from pyfortimanager.models.fortigates import FortiGates
from pyfortimanager.models.fortiswitches_proxy import FortiSwitchesProxy
from pyfortimanager.models.fortiswitches import FortiSwitches
from pyfortimanager.models.install_wizard import InstallWizard
from pyfortimanager.models.metadata_variables import MetadataVariables
from pyfortimanager.models.normalized_interfaces import NormalizedInterfaces
from pyfortimanager.models.policy_packages import PolicyPackages
from pyfortimanager.models.radius_servers import RADIUSServers
from pyfortimanager.models.scripts import Scripts
from pyfortimanager.models.sdwan_templates import SDWANTemplates
from pyfortimanager.models.system import System
from pyfortimanager.models.tasks import Tasks
from pyfortimanager.models.firewall_objects import FirewallObjects


class FortiManager(object):
    """Base API class.
    """

    def __init__(self, host: str, token: str, adom: str = "root", verify: bool = True, proxy_timeout: int = 60, verbose: bool = False, **kwargs):
        self.host = host
        self.token = token
        self.adom = adom
        self.verify = verify
        self.proxy_timeout = proxy_timeout
        self.verbose = verbose

    @property
    def adoms(self):
        """Endpoints related to ADOM management.
        """
        return Adoms(api=self)

    @property
    def cli_template_groups(self):
        """Endpoints related to CLI Template Groups.
        """
        return CLITemplateGroups(api=self)

    @property
    def cli_templates(self):
        """Endpoints related to CLI Templates.
        """
        return CLITemplates(api=self)

    @property
    def device_groups(self):
        """Endpoints related to Device Groups.
        """
        return DeviceGroups(api=self)

    @property
    def fortiaps_proxy(self):
        """Endpoints related to FortiAP proxy calls on a FortiGate.
        """
        return FortiAPsProxy(api=self)

    @property
    def fortiaps(self):
        """Endpoints related to FortiAP management.
        """
        return FortiAPs(api=self)

    @property
    def fortigates_proxy(self):
        """Endpoints related to proxy calls on a FortiGate.
        """
        return FortiGatesProxy(api=self)

    @property
    def fortigates(self):
        """Endpoints related to FortiGate management.
        """
        return FortiGates(api=self)

    @property
    def fortiswitches_proxy(self):
        """Endpoints related to FortiSwitch proxy calls on a FortiGate.
        """
        return FortiSwitchesProxy(api=self)

    @property
    def fortiswitches(self):
        """Endpoints related to FortiSwitch management.
        """
        return FortiSwitches(api=self)

    @property
    def install_wizard(self):
        """Endpoints related to the Install Wizard.
        """
        return InstallWizard(api=self)

    @property
    def metadata_variables(self):
        """Endpoints related to Metadata Variables.
        """
        return MetadataVariables(api=self)

    @property
    def policy_packages(self):
        """Endpoints related to Policy Packages.
        """
        return PolicyPackages(api=self)

    @property
    def radius_servers(self):
        """Endpoints related to RADIUS_Servers.
        """
        return RADIUSServers(api=self)

    @property
    def scripts(self):
        """Endpoints related to Scripts.
        """
        return Scripts(api=self)

    @property
    def sdwan_templates(self):
        """Endpoints related to SD-WAN Templates.
        """
        return SDWANTemplates(api=self)

    @property
    def system(self):
        """Endpoints related to the FortiManager system.
        """
        return System(api=self)

    @property
    def dpp(self):
        """Endpoints related to Dynamic Ports Policies on the build in switch controller
        """
        return DynamicPortPolicy(api=self)
    
    @property
    def normalized_interfaces(self):
        """Endpoints related to Normalized Interfaces.
        """
        return NormalizedInterfaces(api=self)

    @property
    def tasks(self):
        """Endpoints related to tasks
        """
        return Tasks(api=self)

    @property
    def firewall_objects(self):
        """Endpoints related to Firewall Objects.
        """
        return FirewallObjects(api=self)