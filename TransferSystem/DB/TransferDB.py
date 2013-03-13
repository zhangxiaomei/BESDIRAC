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
TransFileListEntry = namedtuple('TransFileListEntry',
                                [#'id',
                                 'LFN',
                                 'trans_req_id',
                                 'start_time',
                                 'finish_time',
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
    if not res["OK"]:
      return res
    res = self._query("select last_insert_id()")
    return res

  def get_TransferRequest(self, condDict = None):
    res = self.getFields( self.tables["TransferRequest"],
                          outFields = TransRequestEntry._fields,
                          condDict = condDict,
                          )
    return res

  def insert_PerTransferFile(self, entry):
    if not isinstance(entry, TransFileListEntry):
      raise TypeError("entry should be TransFileListEntry")
    infoDict = entry._asdict()
    res = self.insertFields( self.tables["TransferFileList"],
                             inDict = infoDict)
    if not res["OK"]:
      return res
    res = self._query("select last_insert_id()")
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
  res = gDB.insert_TransferRequest(entry)
  trans_id = 1
  if not res["OK"]:
    trans_id = res["Value"]
  print gDB.get_TransferRequest()
  print gDB.get_TransferRequest(condDict = {"id":1})

  entry = TransFileListEntry(LFN = "/path/does/not/exist",
                             trans_req_id = trans_id,
                             start_time = None,
                             finish_time = None,
                             status = "new",
                             )
  gDB.insert_PerTransferFile(entry)
