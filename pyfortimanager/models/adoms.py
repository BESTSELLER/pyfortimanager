from pyfortimanager.core.fortimanager import FortiManager


class ADOMs(FortiManager):
    """API class for ADOM management.
    """

    def __init__(self, **kwargs):
        super(ADOMs, self).__init__(**kwargs)

    def all(self, name: str = None):
        """Retrieves all ADOMs or a single ADOM.

        Args:
            name (str): Name of a ADOM.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvmdb/adom"
        }

        # Retrieve a specific ADOM
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def lock(self, name: str):
        """Locks an ADOM.

        Args:
            name (str): Name of the ADOM to lock.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{name}/workspace/lock"
        }

        return self.post(method="exec", params=params)

    def unlock(self, name: str):
        """Unlocks an ADOM.

        Args:
            name (str): Name of the ADOM to unlock.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{name}/workspace/unlock"
        }

        return self.post(method="exec", params=params)

    def commit(self, name: str):
        """Commit changes to an entire ADOM.

        Args:
            name (str): Name of the ADOM to commit changes in.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{name}/workspace/commit"
        }

        return self.post(method="exec", params=params)
