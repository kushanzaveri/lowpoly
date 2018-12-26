from imageview import ImageView
import utils as u
from bokeh.plotting import figure, ColumnDataSource
import matplotlib.image as mpimg

data_uri = "data:image/png;base64,iVBORw0KGg..."

def getImageData(imgView):
    print imgView.source.data['url']
    return 3





    # imageview
    # print "PROCESSING.........."
    # src = get_data_source()
    # if src is not None:
    #     data_uri = src.data['url'][0]
    #     print type(src)
    #     print type(data_uri)
    #     if data_uri is not None:
    #         img_data = mpimg.imread(data_uri.decode('base64'))
    #         print type(img_data)
    #     else:
    #         print "Url is none.........."
    # else:
    #     print "Source is none.........."



