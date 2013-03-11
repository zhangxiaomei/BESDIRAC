# -*- coding: utf-8 -*-

from DIRAC import gLogger, gConfig, S_OK, S_ERROR
from DIRAC.Core.DISET.RequestHandler import RequestHandler

def initializeTransferRequestHandler(serviceInfo):
  """ initialize handler """

  gLogger.info("Initialize TransferRequestHandler.")

  return S_OK()

class TransferRequestHandler(RequestHandler):
  """
  This is for:
    * create a request to transfer data
  """

  types_serverIsOK = []
  def export_serverIsOK(self):
    return S_OK()
