#-*- coding: utf-8 -*-

from dirac.lib.base import *
from dirac.lib.webBase import defaultRedirect
import dirac.lib.credentials as credentials

class InfoController(BaseController):

  def index(self):
    return render("/transfer/info.mako")

  @jsonify
  def getInfoList(self):
    realdata = [
        {"FuncName":"ListRequest", "ScriptName":"besdirac-transfer-list-request.py"} 
        ]
    data = { 'numRecords': len(realdata),
             'functions': realdata}
    return data
