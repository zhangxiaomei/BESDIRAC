# -*- coding: utf-8 -*-

import DIRAC
from DIRAC.Core.Base import Script

Script.setUsageMessage("""
Create a data transfer request.

Usage:
  %s <dataset name> <src SE> <dst SE>
""" % Script.scriptName)

Script.parseCommandLine( ignoreErrors = True )

args = Script.getPositionalArgs()
if (len(args) != 3):
  gLogger.error("Please support dataset name, src SE, dst SE.")
  DIRAC.exit(-1)

from DIRAC.Core.DISET.RPCClient import RPCClient

transferRequest = RPCClient("Transfer/TransferRequest")

dataset = args[0]
ep_from = args[1]
ep_to = args[2]

print transferRequest.create(dataset, ep_from, ep_to)

