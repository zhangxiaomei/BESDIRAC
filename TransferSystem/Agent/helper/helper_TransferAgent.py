# -*- coding: utf-8 -*-

from DIRAC import gLogger, gConfig, S_OK, S_ERROR

class helper_TransferAgent(object):

  def __init__(self, gTransferDB):
    self.transferDB = gTransferDB

  def helper_add_transfer(self, result):
    if not result:
      return False

    self.helper_status_update(
        self.transferDB.tables["TransferFileList"],
        result.id,
        "transfer")

    return True

  def helper_get_new_request(self):
    # 1. get the *new* File in the <<Transfer File List>>.
    #    if we get, goto <<Add New Transfer>>
    result = self.helper_get_new_File()
    if result:
      return result
    # 2. if we can't get, use should get a *new* request
    #    from the <<Transfer Request>>.
    #    if we can't get, return False. STOP
    result = self.helper_get_new_request_entry()
    if not result:
      return result
    # 3. add the filelist in the dataset to the << Transfer File List >>
    condDict = {"name":result.dataset}  
    res = self.transferDB.get_Dataset(condDict)
    if not res["OK"]:
      gLogger.error(res)
      return None
    filelist = res["Value"]
    # update the status in << Request >>
    if len(filelist) > 0:
      req_status = "transfer"
    else:
      req_status = "finish"
    self.helper_status_update(self.transferDB.tables["TransferRequest"],
                              result.id,
                              req_status)
    self.transferDB.insert_TransferFileList(result.id, filelist)
    # 4. get the *new* File Again.
    # 5. can't get, return False. STOP
    result = self.helper_get_new_File()
    return result

  def helper_get_new_request_entry(self):
    """
    TransRequestEntryWithID(
      id=1L, 
      username='lintao', 
      dataset='my-dataset', 
      srcSE='IHEP-USER', 
      dstSE='IHEPD-USER', 
      submit_time=datetime.datetime(2013, 3, 13, 20, 9, 34), 
      status='new')
    """
    condDict = {"status": "new"}
    res = self.transferDB.get_TransferRequest(condDict)
    if not res["OK"]:
      return None
    req_list = res["Value"]
    if len(req_list):
      from BESDIRAC.TransferSystem.DB.TransferDB import TransRequestEntryWithID
      return TransRequestEntryWithID._make(req_list[0])
    pass

  def helper_get_new_File(self):
    """
    >>> helper.helper_get_new_File()
    TransFileListEntryWithID(
      id=1L, 
      LFN='/path/does/not/exist', 
      trans_req_id=1L, 
      start_time=None, 
      finish_time=None, 
      status='new')
    """
    condDict = {"status": "new"}
    res = self.transferDB.get_TransferFileList(condDict)
    if not res["OK"]:
      gLogger.error(res)
      return None
    filelist = res["Value"]
    if len(filelist) > 0:
      gLogger.info("get file entry", filelist[0])
      from BESDIRAC.TransferSystem.DB.TransferDB import TransFileListEntryWithID
      return TransFileListEntryWithID._make(filelist[0])
    return None

  def helper_status_update(self, table, id, toStatus):
    res = self.transferDB.updateFields(
                              table,
                              updateFields = ("status",),
                              updateValues = (toStatus,),
                              condDict = {"id":id},
                              )
    print res

if __name__ == "__main__":
  from DIRAC.Core.Base import Script
  Script.parseCommandLine( ignoreErrors = True )

  from BESDIRAC.TransferSystem.DB.TransferDB import TransferDB 
  gTransferDB = TransferDB()
  helper = helper_TransferAgent(gTransferDB)
  entry = helper.helper_get_new_File()
  print helper.helper_get_new_request_entry()

  if entry:
    print helper.helper_status_update( table = "TransferFileList", 
                                       id = entry.id,
                                       toStatus = "transfer")

  pass
