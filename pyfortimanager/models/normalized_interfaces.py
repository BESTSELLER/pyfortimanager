from pyfortimanager.core.api import BaseModel


class NormalizedInterfaces(BaseModel):
    """API class for Normalized Interfaces in Policy and Objects.
    """

    def __init__(self, **kwargs):
        super(NormalizedInterfaces, self).__init__(**kwargs)

    def delete(self, names: list[str], adom: str = None):
        """Deletes a dyanmic interface

        Args:
            name (str): Name of the dynamic interface
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/dynamic/interface",
            "confirm": 1,
            "filter": [
                "name",
                "in",
                *names
            ],
        }

        return self.post(method="delete", params=params)
