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
    acts_on = ["executable"]
    description = "Extract EXIF and other metadata using Phil Harvey's exiftool"

    def initialize(self):
        if not HAVE_REQUESTS:
            raise ModuleInitializationError(self, "Missing dependency: yara")

        self.results = {}

    def each(self, target):
        '''
        self.results = {
            'macros': u'',
            'analysis': {
                'AutoExec': [],
                'Suspicious': [],
                'IOC': [],
                'Hex String': [],
                'Base64 String': [],
                'Dridex string': [],
                'VBA string': [],
                'Form String': []
            }
        }
        '''
        match_result = False
        exiftool_path = "/usr/bin/exiftool"
        args = [exiftool_path,'-json', target]

        # Run exiftool binary
        host = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
        res = json.loads(host.decode('utf-8'))[0]
        for key,value in res:
            self.results[key].append((value))
        return True











