import os
import subprocess
import json
import hashlib

from fame.core.module import ProcessingModule
from fame.common.utils import tempdir
from fame.common.exceptions import ModuleInitializationError

try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    HAVE_REQUESTS = False

class EXIF_Analysis(ProcessingModule):
    name = "exif-tool"
    description = "Extract EXIF and other metadata using Phil Harvey's exiftool"

    def initialize(self):
        if not HAVE_REQUESTS:
            raise ModuleInitializationError(self, "Missing dependency: yara")

        self.results = {}

    def each_with_type(self, target, file_type):
        self.results = []
        match_result = False
        exiftool_path = "/usr/bin/exiftool"

        if file_type=='executable':
            args = [exiftool_path, '-json', target]

            # Run exiftool binary
            proc = subprocess.Popen(args, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            output = proc.communicate()[0]

            self.results = json.loads(output.decode('utf-8'))[0]

            return True











