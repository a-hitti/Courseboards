#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from base import base

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1300132355.009
__CHEETAH_genTimestamp__ = 'Mon Mar 14 15:52:35 2011'
__CHEETAH_src__ = 'view_post.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Mar 14 14:08:04 2011'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class view_post(base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(view_post, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def title(self, **KWS):



        ## CHEETAH: generated from #def title at line 3, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''Viewing post number ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"post_num",True) # u'$post_num' on line 4, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$post_num')) # from line 4, col 21.
        write(u''' in ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"board.board_name",True) # u'$board.board_name' on line 4, col 34
        if _v is not None: write(_filter(_v, rawExpr=u'$board.board_name')) # from line 4, col 34.
        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def content(self, **KWS):



        ## CHEETAH: generated from #def content at line 7, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<a href="/view_board/''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"board.key",True) # u'$board.key' on line 8, col 22
        if _v is not None: write(_filter(_v, rawExpr=u'$board.key')) # from line 8, col 22.
        write(u'''"><img src="/static/images/arrow-left-24.png" alt="Back"> Back</a>

<form action="/new_reply/" method="post">
\t<!--<input type="text" name="reply_text" size="10" />-->
\t<TEXTAREA NAME="reply_text" COLS=60 ROWS=6"></TEXTAREA><br>
\t<input type="hidden" name="board_key" value="''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"board.key",True) # u'$board.key' on line 13, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$board.key')) # from line 13, col 47.
        write(u'''">
\t<input type="hidden" name="post_num" value="''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"post_num",True) # u'$post_num' on line 14, col 46
        if _v is not None: write(_filter(_v, rawExpr=u'$post_num')) # from line 14, col 46.
        write(u'''">
\t<input type="submit" value="Reply" />
</form>
\t<div class="message">
\t\t''')
        _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"board",True),"posts",True)[VFSL([locals()]+SL+[globals(), builtin],"post_num",True)],"message",True) # u'$board.posts[$post_num].message' on line 18, col 3
        if _v is not None: write(_filter(_v, rawExpr=u'$board.posts[$post_num].message')) # from line 18, col 3.
        write(u'''
\t</div><br />
\t''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"board",True),"posts",True)[VFSL([locals()]+SL+[globals(), builtin],"post_num",True)],"replies",True)) # u'$len($board.posts[$post_num].replies)' on line 20, col 2
        if _v is not None: write(_filter(_v, rawExpr=u'$len($board.posts[$post_num].replies)')) # from line 20, col 2.
        write(u''' replies:<br/>
''')
        for reply in VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"board",True),"posts",True)[VFSL([locals()]+SL+[globals(), builtin],"post_num",True)],"replies",True): # generated from line 21, col 1
            write(u'''\t<div class="reply">
\t\t''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"reply",True)['reply-text'] # u"$reply['reply-text']" on line 23, col 3
            if _v is not None: write(_filter(_v, rawExpr=u"$reply['reply-text']")) # from line 23, col 3.
            write(u'''
\t</div>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''

''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_view_post= 'writeBody'

## END CLASS DEFINITION

if not hasattr(view_post, '_initCheetahAttributes'):
    templateAPIClass = getattr(view_post, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(view_post)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=view_post()).run()


