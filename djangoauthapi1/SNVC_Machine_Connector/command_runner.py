from pprint import pprint


def execute_command(ssh_client, command):
    try:
        
        # Execute the command
        stdin, stdout, stderr = ssh_client.exec_command(command+" 2>&1",timeout=5)
        # Read the output
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Print the output
        pprint(error)
        pprint(output)

        return output
    except Exception as e:
        print("Error: Failed to execute command on the VM:", str(e))
        return None

