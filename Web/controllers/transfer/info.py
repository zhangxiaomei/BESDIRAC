#-*- coding: utf-8 -*-

from dirac.lib.base import *
from dirac.lib.webBase import defaultRedirect
import dirac.lib.credentials as credentials

class InfoController(BaseController):

  def index(self):
    return render("/transfer/info.mako")
