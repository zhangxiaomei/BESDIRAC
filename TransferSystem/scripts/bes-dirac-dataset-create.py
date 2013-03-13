# -*- coding: utf-8 -*-

import DIRAC
from DIRAC.Core.Base import Script

Script.parseCommandLine( ignoreErrors = True )

from DIRAC.Core.DISET.RPCClient import RPCClient

transferRequest = RPCClient("Transfer/Dataset")

dataset = "my-dataset"
filelist = map(str, range(10))
print transferRequest.create(dataset, filelist)

