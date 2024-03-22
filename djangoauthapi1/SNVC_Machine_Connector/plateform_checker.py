import platform


class PlaformInfo:
    """
    Class PlaformInfo to represent the platform type
    """
    operating_system = platform.system()

    @classmethod
    def is_windows(cls):
        """
        Check windows platform
        """
        return cls.operating_system == 'Windows'

    @classmethod
    def is_mac(cls):
        """
        Check mac platform
        """
        return cls.operating_system == 'Darwin'

    @classmethod
    def is_linux(cls):
        """
        Check linux platform
        """
        return cls.operating_system == 'Linux'
