# -*- coding: utf-8 -*-

from DIRAC import gLogger, gConfig, S_OK, S_ERROR
from DIRAC.Core.Base.AgentModule import AgentModule

class TransferAgent(AgentModule):

  def initialize(self):
    self.count = 0

    return S_OK()

  def execute(self):

    gLogger.info("execute: ", self.count)

    self.count += 1

    return S_OK()
