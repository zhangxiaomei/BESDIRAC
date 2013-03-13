# -*- coding: utf-8 -*-

import DIRAC
from DIRAC.Core.Base import Script

Script.parseCommandLine( ignoreErrors = True )

from DIRAC.Core.DISET.RPCClient import RPCClient

transferRequest = RPCClient("Transfer/TransferRequest")

dataset = "my-dataset"
ep_from = "IHEP-USER"
ep_to = "IHEPD-USER"
print transferRequest.create(dataset, ep_from, ep_to)

