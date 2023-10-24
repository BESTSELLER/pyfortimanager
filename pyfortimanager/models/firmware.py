from pyfortimanager.core.fortimanager import FortiManager


class Firmware(FortiManager):
    """API class for Firmware.
    """

    def __init__(self, **kwargs):
        super(Firmware, self).__init__(**kwargs)

    def all(self, platform: str=None, product: str=None):
        """Retrieves all available firmware versions for all or a specific product line.

        Args:
            platform (str, optional): Model number of a specific product type. Ex. FortiAP-U432F.
            product (str, optional): A specific product group. Ex. FMG, FGT, FSW, FAP, etc.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/um/image/version/list",
            "data":
                {
                    "platform": platform,
                    "product": product
                }
        }

        return self.post(method="exec", params=params)