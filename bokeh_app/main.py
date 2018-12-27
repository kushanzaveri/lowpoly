from bokeh.io import curdoc
from bokeh.models.widgets import Button
from bokeh.layouts import row, column

from core_new import Core
from imageview import ImageView
import utils as u

imgView = ImageView()
imgViewLayout = imgView.getView()
core = Core(imgView)
coreLayout = core.getView()

curdoc().add_root(row(imgViewLayout, coreLayout))
