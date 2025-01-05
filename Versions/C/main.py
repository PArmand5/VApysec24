import subprocess
import json

from libs.Checklist import (
    check_bitlocker_status,
    check_configured_users,
    check_msdefender_status,
    check_winfirewall_status,
    check_drive_status,
    check_last_update_status,
    get_mpcomputerstatus
)

# Define a list of servers (for local operations, this is just your local machine)
servers = ["localhost"]

results = []
server_data_template = {
    "HOST": "",
    "IDENTITY": "",
    "VERSION_CODENAME": ""
}

for server in servers:
    try:
        # Get the username of the logged-in user
        identity_result = subprocess.check_output("whoami", shell=True, text=True).strip()

        # Get Windows version codename
        version_command = "wmic os get Caption /value"
        version_result = subprocess.check_output(version_command, shell=True, text=True).strip()
        version_codename = (
            version_result.split("=")[-1].strip() if "=" in version_result else "Unknown"
        )

        # Initialize server data
        server_data = server_data_template.copy()
        server_data["HOST"] = server
        server_data["IDENTITY"] = identity_result
        server_data["VERSION_CODENAME"] = version_codename

        # Checklist operations (adjust to work locally)
        print("Running checklist operations...")
        check_bitlocker_status()  # Adjust or mock if needed
        check_configured_users()  # Adjust or mock if needed
        check_msdefender_status()  # Adjust or mock if needed
        check_winfirewall_status()  # Adjust or mock if needed
        check_drive_status()  # Adjust or mock if needed
        check_last_update_status()  # Adjust or mock if needed
        mp_status = get_mpcomputerstatus()  # Adjust or mock if needed
        print(f"Microsoft Protection Status: {mp_status}")

        # Add server data to results
        results.append(server_data)

    except Exception as e:
        print(f"Error retrieving data for {server}: {str(e)}")

# Output the results as a JSON string
print(json.dumps(results, indent=4))