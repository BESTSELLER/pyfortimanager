import time
from pyfortimanager.core.api import BaseModel


class Tasks(BaseModel):
    """API class for calls to FortiGates config
    """

    def __init__(self, **kwargs):
        super(Tasks, self).__init__(**kwargs)

    def get(self, task: int = None, filter: list = None, loadsub: bool = True):
        """Retrieves all FortiManager tasks or a single task.

        Args:
            task (int): ID of a specific task.
            filter (list): Filter the result according to a set of criteria. example: List [ "{attribute}", "==", "{value}" ]
            loadsub (bool): Enable or disable the return of any sub-objects. Default is enabled.

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

    def wait(self, task_id: str, interval: int = 1, max_wait_time: int = 300) -> bool:
        """Waits for a given task to finish

        Args:
            task_id (int): ID of a specific task

        Returns:
            bool: True if success full, False on error or timeout
        """
        start_time = time.time()
        while(True):
            if time.time() - start_time > max_wait_time:
                return False

            task = self.get(task_id)
            for result in task.data:
                if result["percent"] == 100 and result["state"] >= 5:
                    return False
                
                if result["percent"] == 100 and result["state"] <= 4:
                    return True
                
            time.sleep(interval)
