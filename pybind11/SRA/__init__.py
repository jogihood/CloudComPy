#!/usr/bin/env python3

##########################################################################
#                                                                        #
#                              CloudComPy                                #
#                                                                        #
#  This program is free software; you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation; either version 3 of the License, or     #
#  any later version.                                                    #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program. If not, see <https://www.gnu.org/licenses/>. #
#                                                                        #
#          Copyright 2020-2021 Paul RASCLE www.openfields.fr             #
#                                                                        #
##########################################################################

"""
SRA is a standard plugin of cloudComPy.

The availability of the plugin can be tested with the :py:meth:`cloudComPy.isPluginSRA` function:
::

  isSRA_available = cc.isPluginSRA()

SRA is a submodule of cloudCompy:
::

  import cloudComPy as cc
  # ...
  if cc.isPluginSRA():
      import cloudComPy.SRA
      cc.SRA.loadProfile(...)
"""
from _SRA import *
initTrace_SRA()
