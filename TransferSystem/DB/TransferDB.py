# -*- coding: utf-8 -*-

from DIRAC import gLogger, gConfig, S_OK, S_ERROR, Time
from DIRAC.Core.Base.DB import DB

# Some basic arguments will use namedtuple 
from collections import namedtuple
import datetime

TransRequestEntry = namedtuple('TransRequestEntry',
                              [#'id',
                               'username',
                               'dataset',
                               'srcSE',
                               'dstSE',
                               'submit_time',
                               'status',
                               ])

class TransferDB(DB):
  tables = dict(TransferRequest = "TransferRequest",
                TransferFileList = "TransferFileList")

  def __init__(self, dbname="TransferDB", 
                     fullname="Transfer/TransferDB",
                     maxQueueSize = 10):
    DB.__init__(self, dbname, fullname, maxQueueSize)

  def insert_TransferRequest(self, entry):
    if not isinstance(entry, TransRequestEntry):
      raise TypeError("entry should be TransRequestEntry")
    infoDict = entry._asdict()
    res = self.insertFields( self.tables["TransferRequest"],
                             inDict = infoDict)
    return res

if __name__ == "__main__":
  from DIRAC.Core.Base import Script
  Script.parseCommandLine( ignoreErrors = True )

  gDB = TransferDB()

  entry = TransRequestEntry(username = "lintao", 
                            dataset = "my-dataset",
                            srcSE = "IHEP-USER",
                            dstSE = "IHEPD-USER",
                            status = "new",
                            submit_time = datetime.datetime.now())
  gDB.insert_TransferRequest(entry)
