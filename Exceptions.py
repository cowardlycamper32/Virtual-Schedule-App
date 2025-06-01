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


class InvalidTaskException(BugReportException):
    """
    Task is not valid or is incorrect. Please make a bug report with details of what task you were using.
    """
    pass

class InvalidScoreException(BugReportException):
    """
    Score is not valid or is incorrect. Please make a bug report.
    """