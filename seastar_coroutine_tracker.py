#!/usr/bin/env python3
#!/usr/bin/env python3
import gdb
import requests
import json

class TrackCoroutines(gdb.Command):
    """Track Seastar coroutines."""

    def __init__(self):
        super(TrackCoroutines, self).__init__("track-coroutines", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        tasks_info = [

            {"address": "0x123456", "func": "coroutine_func", "state": "running", "execution_time_ns": 1000},
            # Add more coroutine info as needed
        ]

        data_json = json.dumps(tasks_info)

        print(f"Sending data: {data_json}")  # Debug line
        # Send data via HTTP POST without waiting for a response
        try:
            requests.post('http://127.0.0.1:5000/update', json=tasks_info, timeout=0.1)
        except requests.exceptions.RequestException as e:

            print(f"Error sending data: {e}")


TrackCoroutines()

