# -*- coding: utf-8 -*-

import datetime

from DIRAC import gLogger, gConfig, S_OK, S_ERROR
from DIRAC.Core.DISET.RequestHandler import RequestHandler

from BESDIRAC.TransferSystem.DB.TransferDB import TransRequestEntry

tmpGlobalStore = {}

global gTransferDB 

def initializeTransferRequestHandler(serviceInfo):
  """ initialize handler """

  gLogger.info("Initialize TransferRequestHandler.")

  from BESDIRAC.TransferSystem.DB.TransferDB import TransferDB

  global gTransferDB

  gTransferDB = TransferDB()

  return S_OK()

class TransferRequestHandler(RequestHandler):
  """
  This is for:
    * create a request to transfer data
  """

  def initialize(self):
    credDict = self.getRemoteCredentials()
    gLogger.info(credDict)
    self.user = credDict["username"]

    tmpGlobalStore.setdefault( self.user, 
                              {"endpoint":{}
                              } )

  types_serverIsOK = []
  def export_serverIsOK(self):
    return S_OK()

  types_getEndPoint = []
  def export_getEndPoint(self):
    ep = tmpGlobalStore[self.user]["endpoint"]

    return S_OK( ep )

  types_setEndPoint = [str, str]
  def export_setEndPoint(self, name, url):
    gLogger.info(name)
    gLogger.info(url)

    tmpGlobalStore[self.user]["endpoint"][name] = url

    return S_OK()

  types_create = [ str, str, str ]
  def export_create(self, dataset, ep_from, ep_to):
    entry = TransRequestEntry(username = self.user, 
                              dataset = dataset,
                              srcSE = ep_from,
                              dstSE = ep_to,
                              status = "new",
                              submit_time = datetime.datetime.now())
    gLogger.info("create an Entry:", entry)
    res = gTransferDB.insert_TransferRequest(entry)
    if not res["OK"]:
      return res
    return S_OK()
