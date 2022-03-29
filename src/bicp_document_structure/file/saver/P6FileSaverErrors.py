import json
from pathlib import Path
from typing import Optional

from bicp_document_structure.util.report.error.ErrorHeader import ErrorHeader
from bicp_document_structure.util.report.error.ErrorReport import ErrorReport

__errPrefix = "p6FileSaverError"


def errPrefix():
    return __errPrefix


class P6FileSaverErrors:
    class UnableToAccessPath:
        header = ErrorHeader(errPrefix() + "0", "unable to access path")

        class Data:
            def __init__(self, path: Path, exception: Exception = None):
                self.path: Path = path
                self.exception: Exception = exception

            def __str__(self):
                return json.dumps({
                    "path": str(self.path)
                })

    class UnableToWriteFile:
        header = ErrorHeader(errPrefix() + "1", "unable to write file")

        class Data:
            def __init__(self, path: Path, exception: Exception = None):
                self.path: Path = path
                self.exception: Exception = exception

            def __str__(self):
                return json.dumps({
                    "path": str(self.path)
                })

