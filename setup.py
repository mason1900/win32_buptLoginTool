from distutils.core import setup
import py2exe

setup(
    name = 'buptLogintool',
    description = 'buptLoginTool',
    version = '1.0',

    windows = [
                  {
                      'script': 'LoginToolUI.py',
                      'icon_resources': [(1, "logo.ico")],
                  }
              ],

    options = {
                  'py2exe': {
#                      以下两行为pyGTK程序的通用配置，为节省空间本程序删去了部分用不到的库文件
#                      'packages':'encodings',
#                      'includes': 'cairo, pango, pangocairo, atk, gobject, gio',
                       'includes': 'cairo, pango, gio, pangocairo, atk',
                  }
              },

    data_files=[
                   'ui.glade','logo.ico',
                   'readme.md'
               ]
)