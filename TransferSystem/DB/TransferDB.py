# -*- coding: utf-8 -*-

from DIRAC import gLogger, gConfig, S_OK, S_ERROR, Time
from DIRAC.Core.Base.DB import DB

class TransferDB(DB):

  def __init__(self, dbname="TransferDB", fullname="Transfer/TransferDB"):
    DB.__init__(self, dbname, fullname)
