# -*- coding: utf-8 -*-

### Before running this in a python command prompt 
##  use this hack to enable  encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#import pywinauto
from pywinauto import Application

app = Application(backend="uia").start("notepad.exe")  # we'll lose a lot of controls without backend="uia" !

#app.window(title_re=u'\u05dc.*').dump_tree   # short for print_ctrl_ids()
#window(title=u'\u05e2\u05e8\u05d9\u05db\u05d4').select()

# n for notepad  :)
n=app.window(title_re=u'\u05dc.*')
n.Edit1.type_keys('xxxxx@sina.com')

n.MenuItem6.click_input()
'''
OR use this to get to the Help ('Ezra') menu in Hebrew:
n[u'\u05e2\u05d6\u05e8\u05d4'].click_input()
'''

# Click on About ('Odot') menu in Hebrew
n.child_window(title_re=u'\u05D0.*', control_type='MenuItem').invoke()
