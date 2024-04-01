import paramiko

from .check_vm_platform import PlaformInfo as pi
from .command_runner import execute_command
from .create_log_report import generate_log_report
from .envoirnment_setup import Environment


def connect_to_vm(server_ip: str | None = None,
                  server_username: str | None = None,
                  server_password: str | None = None,
                  pike_log_level: str = "debug",
                  pike_share: str = "sambashare",
                  client_ip: str | None = None,
                  client_username: str | None = None,
                  client_password: str | None = None,
                  suite_name: str | None = None):
    """
    This function is responsible for the connecting with client
    vm and perform setup operations and run test suite.
    :param pike_log_level:
    :param pike_share:
    :param vm_ip:
    :param username:
    :param password:
    :param suite_name:
    :return: None
    """
    try:
        # Create a new SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to the VM
        ssh_client.connect(hostname=client_ip, username=client_username, password=client_password)
        print("Connected to the VM successfully.")
        ev_setup = Environment(ssh_client=ssh_client,
                               SERVER_IP=server_ip,
                               SERVER_USERNAME=server_username,
                               SERVER_PASSWORD=server_password,
                               PIKE_LOGLEVEL=pike_log_level,
                               PIKE_SHARE=pike_share)
        if pi.is_linux(ssh_client=ssh_client):
            # check if suite name is equal to your original suite
            if suite_name == "test_file_supersede_and_file_create":
                command_to_run = ev_setup.export_environment_for_linux(suite_name)
            elif suite_name == "test_updation":
                command_to_run = "command for run updation suite"
                # execute_command(ssh_client,cmd)
        elif pi.is_windows(ssh_client):
            # check if suite name is equal to your original suite
            if suite_name == "test_creation":
                command_to_run = fr"python C:\Users\Administrator\snvc-interop\tools\pike\src\pike\test\test_shivam.py"
            elif suite_name == "test_updation":
                command_to_run = "command for run updation suite"
        else:
            command_to_run = "mac_command"
        output = execute_command(ssh_client, command_to_run)
        generate_log_report(output, suite_name)
        if "OK" in output:
            return "Test Suite Passed"
        elif "FAILED" in output:
            return "Test Suite Failed"
        else:
            return "No Output"

        # return ssh_client
    except paramiko.AuthenticationException:
        return "Authentication failed, please verify your credentials."
    except paramiko.SSHException as ssh_exception:
        return f"Unable to establish SSH connection: {ssh_exception}"
    except Exception:
        return "Other error"
    finally:
        # Close the SSH connection
        ssh_client.close()