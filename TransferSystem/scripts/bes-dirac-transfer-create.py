# -*- coding: utf-8 -*-

import DIRAC
from DIRAC.Core.Base import Script

Script.parseCommandLine( ignoreErrors = True )

from DIRAC.Core.DISET.RPCClient import RPCClient

transferRequest = RPCClient("Transfer/TransferRequest")

filelist = [str(i) for i in xrange(10)]
ep_from = "ep_from"
ep_to = "ep_to"
print transferRequest.create(filelist, ep_from, ep_to)

