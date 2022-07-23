import sys
import pyqrcode
import png
from pyqrcode import QRCode

link = sys.argv[1]
url = pyqrcode.create(link)
url.png('output.png', scale=10)
