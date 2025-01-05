import subprocess

def execute_command(command):
    """Helper function to execute a shell command and return the output."""
    try:
        result = subprocess.check_output(command, shell=True, text=True).strip()
        print(result)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(f"Error: {e}")
        return None

def check_configured_users():
    """Gather configured users."""
    print("Gathering configured users...")
    command = "net user"
    return execute_command(command)

def check_bitlocker_status():
    """Check the status of BitLocker."""
    print("Checking BitLocker status...")
    command = "manage-bde -status"
    return execute_command(command)

def check_msdefender_status():
    command = "manage-bde -status"
    result = subprocess.check_output(command, shell=True, text=True).strip()
    print(result)
    return result
    

def check_winfirewall_status():
    """Check the status of Windows Firewall."""
    print("Checking Windows Firewall status...")
    command = "netsh advfirewall show allprofiles state"
    return execute_command(command)

def check_drive_status():
    """Check drive and mount status."""
    print("Checking drive and mount status...")
    command = 'powershell -Command "Get-PSDrive"'
    return execute_command(command)

def check_last_update_status():
    """Check when Windows was last updated."""
    print("Checking last update status...")
    command = 'powershell -Command "Get-HotFix | Select-Object -First 5"'
    return execute_command(command)

def get_mpcomputerstatus():
    """Get various computer stats."""
    print("Getting Microsoft Protection computer status...")
    command = 'powershell -Command "Get-MpComputerStatus"'
    return execute_command(command)
