from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

from scripts.core import core_tab

tab = core_tab()

# tabs = Tabs(tabs =[tab])
curdoc().add_root(tab)
