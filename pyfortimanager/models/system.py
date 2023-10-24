from pyfortimanager.core.fortimanager import FortiManager


class System(FortiManager):
    """API class for the FortiManager system.
    """

    def __init__(self, **kwargs):
        super(System, self).__init__(**kwargs)
    
    def ha(self):
        """Obtain HA information and status of the system.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/ha/status"
        }

        return self.post(method="get", params=params)

    def reboot(self, message: str=None):
        """Reboots the FortiManager.

        Args:
            message (str, optional): Optional message to be stored in the event log.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/reboot",
            "data": {
                "message": message
            }
        }

        return self.post(method="exec", params=params)

    def status(self):
        """Retrieves the system status.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/sys/status"
        }

        return self.post(method="get", params=params)

    def tasks(self, task:int=None, filter: list=None, loadsub: int=0):
        """Retrieves all tasks or a single task.

        Args:
            task (int): ID of a specific task.
            filter (list): Filter the result according to a set of criteria. example: List [ "{attribute}", "==", "{value}" ]
            loadsub (int): Enable or disable the return of any sub-objects.

        Returns:
            dict: JSON data.
        """
   
        params = {
            "url": "/task/task",
            "filter": filter,
            "loadsub": loadsub
        }

        # Retrieve a single task
        if task:
            params['url'] = f"/task/task/{task}/line"

        return self.post(method="get", params=params)