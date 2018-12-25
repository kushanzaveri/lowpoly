import os
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.plotting import figure
from os.path import join, basename
import logging
import base64
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Button


def file_callback(attr, old, new):
    print "On change callback"
data = {'filename': ["kushan", "wew"]}

source = ColumnDataSource(data = data)

callback = CustomJS(args=dict(source=source), code= """
    var data = source.data
    //console.log(data['filename']);
    console.log(cb_data)
    /*
    var temp = data['filename'][0]
    data['filename'][0] = data['filename'][1];
    data['filename'][1] = temp;
    */
    source.change.emit();
""")

from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Range1d

bosch_logo = "static/tree.jpg"
logo_src = ColumnDataSource(dict(url = [bosch_logo]))

page_logo = figure(plot_width = 500, plot_height = 500, title="")
page_logo.toolbar.logo = None
page_logo.toolbar_location = None
page_logo.x_range=Range1d(start=0, end=1)
page_logo.y_range=Range1d(start=0, end=1)
page_logo.xaxis.visible = None
page_logo.yaxis.visible = None
page_logo.xgrid.grid_line_color = None
page_logo.ygrid.grid_line_color = None
page_logo.image_url(url='url', x=0.05, y = 0.85, h=0.7, w=0.9, source=logo_src)
page_logo.outline_line_alpha = 0
curdoc().add_root(page_logo)
# save_path = os.getcwd()
# name = 'temp.esi'

# def file_callback(attr, old, new):
#     print "On change callback"
    # print attr;
    # print old;
    # print new;
#     raw_contents = source.data['contents'][0]
#     # remove the prefix that JS adds
#     prefix, b64_contents = raw_contents.split(",", 1)
#     file_contents = base64.b64decode(b64_contents)
#     fname = join(save_path, name)
#     print save_path
#     print name
#     print type(file_contents)
#     with open(fname, "wb") as f:
#         f.write(file_contents)
#     logging.info("Success: file uploaded " + fname)
#     update(fname)



button = Button(label="Upload File", button_type="success", callback = callback)
# button.callback = CustomJS(args=dict(source=source), code=_upload_js)
# Set up plot
p = figure(x_range=(0,1), y_range=(0,1))

# def update(fname):
#     p.image_url(url=[fname], x=0, y=1, w=1, h=1)

# update("temp.esi")
curdoc().add_root(row(button, p))
curdoc().title = "Image Loader"
