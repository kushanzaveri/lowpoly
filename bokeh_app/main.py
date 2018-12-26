from bokeh.io import curdoc
from bokeh.models.widgets import Tabs, Button
from bokeh.layouts import row, column

from scripts.core import core
from scripts.imageview import ImageView
from scripts.process import getImageData

import base64
from imageio import imread
import io
import matplotlib.pyplot as plt


# tab = core()
imgView = ImageView()
view = imgView.getView();

def callback():
    print "process...."
    # filename = "images/lake.jpg"
    # with open(filename, "rb") as fid:
    #     data = fid.read()
    # b64_bytes = base64.b64encode(data)
    # b64_string = b64_bytes.decode()
    b64_string = imgView.getName().split(",")[1]
    img = imread(io.BytesIO(base64.b64decode(b64_string)))
    # show image
    # plt.figure()
    # plt.imshow(img)
    # plt.show()
    print img.shape
    print imgView.getName()[:100]
    # print b64_string[:100]
    # b64_string = imgView.getName()
    # img = imread(io.BytesIO(base64.b64decode(b64_string)))  
    # plt.figure()
    # plt.imshow(img, cmap="gray")



button = Button(label="Process...", )
button.on_click(callback);

# tabs = Tabs(tabs =[tab])
curdoc().add_root(row(view,button))
