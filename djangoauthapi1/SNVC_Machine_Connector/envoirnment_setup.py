class Environment:
    """
    Environment class will setup the environment as per different OS.
    """

    def __init__(self, ssh_client,
                 SERVER_IP: str = None,
                 SERVER_USERNAME: str = None,
                 SERVER_PASSWORD: str = None,
                 PIKE_LOGLEVEL: str = None,
                 PIKE_SHARE: str = None,
                 SUITE_NAME: str = None):
        self.ssh_client = ssh_client
        self.SERVER_IP = SERVER_IP
        self.SERVER_USERNAME = SERVER_USERNAME
        self.SERVER_PASSWORD = SERVER_PASSWORD
        self.PIKE_LOGLEVEL = PIKE_LOGLEVEL
        self.PIKE_SHARE = PIKE_SHARE
        self.SUITE_NAME = SUITE_NAME

    def export_environment_for_linux(self,suite_name ):
        """This method will do setup for Linux based VM."""
        commands = [f"export PYTHONPATH='$PYTHONPATH:/c/python_lib'",
                    f'export PIKE_SERVER={self.SERVER_IP}',
                    f'export PIKE_SHARE={self.PIKE_SHARE}',
                    f"export PIKE_CREDS={self.SERVER_USERNAME}%{self.SERVER_PASSWORD}",
                    f"export PIKE_LOGLEVEL={self.PIKE_LOGLEVEL}",
                    "export PIKE_SIGN=yes",
                    "export PIKE_ENCRYPT=no",
                    "export PIKE_MAX_DIALECT=DIALECT_SMB3_1_1",
                    "export PIKE_MIN_DIALECT=DIALECT_SMB2_002",
                    "export PIKE_TRACE=no",
                    fr"python3 -m unittest /home/msys/snvc-interop/tools/pike/src/pike/test/{suite_name}.py"
                    ]
        command_to_run = " && ".join(commands)
        return command_to_run

    def set_environment_for_windows(self):
        """This method will do setup for Linux based VM."""
        commands = ['SETX PYTHONPATH=%PYTHONPATH%;C:\python_lib',
                    f'set PIKE_SERVER={self.SERVER_IP}',
                    f'set PIKE_SHARE={self.PIKE_SHARE}',
                    f"set PIKE_CREDS={self.SERVER_USERNAME}%{self.SERVER_PASSWORD}",
                    f"set PIKE_LOGLEVEL={self.PIKE_LOGLEVEL}",
                    "set PIKE_SIGN=yes",
                    "set PIKE_ENCRYPT=no",
                    "set PIKE_MAX_DIALECT=DIALECT_SMB3_1_1",
                    "set PIKE_MIN_DIALECT=DIALECT_SMB2_002",
                    "set PIKE_TRACE=no",
                    ]
        command_to_run = " & ".join(commands)
        return command_to_run
