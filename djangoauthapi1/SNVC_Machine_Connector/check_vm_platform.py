import platform


class PlaformInfo:
    """
    Class PlaformInfo to represent the platform type
    """
    operating_system = platform.system()

    @classmethod
    def is_windows(cls, ssh_client):
        """
        Check windows platform
        """
        import pdb
        pdb.set_trace()
        stdin, stdout, stderr = ssh_client.exec_command('systeminfo | find "OS Name"')
        system_info = stdout.read().decode().strip().split(':')[1].strip().split()[1]
        return system_info == 'Windows'

    @classmethod
    def is_mac(cls, ssh_client):
        """
        Check mac platform
        """
        return cls.operating_system == 'Darwin'

    @classmethod
    def is_linux(cls, ssh_client):
        """
        Check linux platform
        """
        stdin, stdout, stderr = ssh_client.exec_command('uname')
        system_info = stdout.read().decode().strip()
        return system_info == 'Linux'
