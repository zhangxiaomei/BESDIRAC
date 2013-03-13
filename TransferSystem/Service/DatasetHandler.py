# -*- coding: utf-8 -*-

import datetime

from DIRAC import gLogger, gConfig, S_OK, S_ERROR
from DIRAC.Core.DISET.RequestHandler import RequestHandler

global gTransferDB

def initializeDatasetHandler(serviceInfo):
  """ initialize handler """
  gLogger.info("Initialize Dataset Handler.")

  from BESDIRAC.TransferSystem.DB.TransferDB import TransferDB

  global gTransferDB

  gTransferDB = TransferDB()

  return S_OK()

class DatasetHandler(RequestHandler):
  """
  This is for:
    * create a dataset
  """

  def initialize(self):
    credDict = self.getRemoteCredentials()
    gLogger.info(credDict)
    self.user = credDict["username"]

    return S_OK()

  types_create = [str, list]
  def export_create(self, dataset, filelist):
    gLogger.info("Username: ", self.user)
    gLogger.info("Dataset: ", dataset)
    gLogger.info("Filelist: ", filelist)
    res = gTransferDB.insert_Dataset( dataset, self.user, filelist)

    if not res["OK"]:
      return res

    return S_OK()
