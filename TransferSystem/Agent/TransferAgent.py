# -*- coding: utf-8 -*-

from DIRAC import gLogger, gConfig, S_OK, S_ERROR
from DIRAC.Core.Base.AgentModule import AgentModule

global gTransferDB

class TransferAgent(AgentModule):

  def initialize(self):
    self.count = 0

    self.MAX_TRANSFER = self.am_getOption("MAX_TRANSFER", 2)
    gLogger.info("MAX_TRANSFER: ", self.MAX_TRANSFER)

    self.transfer_worker = []

    global gTransferDB
    from BESDIRAC.TransferSystem.DB.TransferDB import TransferDB
    gTransferDB = TransferDB()

    return S_OK()

  def execute(self):

    gLogger.info("execute: ", self.count)
    self.count += 1

    # Handle the existed transfer worker
    for worker in self.transfer_worker:
      pass
    else:
      # the transfer work are all working
      pass

    # Create new transfer worker
    idle_worker = self.MAX_TRANSFER - len(self.transfer_worker)
    if idle_worker:
      for i in xrange(idle_worker):
        # append a new worker
        # if can't add, just break
        if not self.add_new_transfer():
          break
        gLogger.info("Add a new Transfer")

    return S_OK()

  def add_new_transfer(self):
    """
      if add a new, return true,
      else return false
    """
    # << Get New File >>
    result = self.helper_get_new_request()

    # << Add New Transfer >>
    return self.helper_add_transfer(result)

