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
#                      ��������ΪpyGTK�����ͨ�����ã�Ϊ��ʡ�ռ䱾����ɾȥ�˲����ò����Ŀ��ļ�
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