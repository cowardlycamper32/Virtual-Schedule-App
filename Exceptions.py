class BugReportException(Exception):
    """
    This Shouldn't be possible. Please make a bug report.
    """
    pass

class InvalidConfigPath(BugReportException):
    """
    Config File does not exist. Please make a bug report.
    """

class InvalidPathException(BugReportException):
    """
    Path does not exist. Please make a bug report.
    """