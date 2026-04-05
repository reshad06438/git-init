import subprocess
import json

process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)

if "unauthorized_cryptominer" in process_list.stdout:
    alert_data = {
        "event": "Unauthorized Process",
        "severity": "High",
        "process": "unauthorized_cryptominer"
    }

with open("security_alert.json", "w") as file:
        json.dump(alert_data, file, indent=4)
