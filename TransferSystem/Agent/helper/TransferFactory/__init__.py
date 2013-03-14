#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import subprocess

class TransferFactory(object):
  PROTOCOL = ["DIRACDMS"]

  def generate(self, protocol, info):
    mod = __import__("BESDIRAC.TransferSystem.Agent.helper.TransferFactory.TransferBy%s"%(protocol),
        globals(),
        locals(),
        ["%sTransferWorker"%(protocol)]
        )
    TR = getattr(mod, "%sTransferWorker"%(protocol))
    tr = TR()
    tr.create_popen(info)
    return tr


gTransferFactory = TransferFactory()
