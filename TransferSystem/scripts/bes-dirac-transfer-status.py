# -*- coding: utf-8 -*-

import DIRAC
from DIRAC.Core.Base import Script

Script.parseCommandLine( ignoreErrors = True )

from DIRAC.Core.DISET.RPCClient import RPCClient

transferRequest = RPCClient("Transfer/TransferRequest")

condDict = {}
print transferRequest.status(condDict)

