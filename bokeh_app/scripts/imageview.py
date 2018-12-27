import numpy as np

from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import row, column
from bokeh.models import CustomJS
from bokeh.models.widgets import Button
from bokeh.models.widgets.inputs import TextInput

from .tools.utils import loadImage, adjust_plot, init



class ImageView:
    xmax = 1024
    ymax = 1024
    img_url = "default"
    img_data = None
    offset = 50
    source = ColumnDataSource(data=dict(url=[img_url], xdim = [0], ydim = [0]))
    plot = figure(title= "Original Image")

    # def getName(self):
    #     return self.img_url

    # def getData(self):
    #     return self.img_data

    def getView(self):
        __code__ = """ 
        function read_image(file){
            var reader = new FileReader();
            reader.onload = load_handler;
            reader.onerror = error_handler;
            reader.readAsDataURL(file)
        }
        function getImageDimensions(file) {
            return new Promise (function (resolved, rejected) {
                var i = new Image()
                i.onload = function(){
                    resolved(
                        {w: i.width, h: i.height}
                    )
                };
                i.src = file
            })
        }

        async function load_handler(event) {
            var b64string = event.target.result;
            var dimensions = await getImageDimensions(b64string)            
            source.data['xdim'] = [dimensions.w];
            source.data['ydim'] = [dimensions.h];
            source.data['url'] = [b64string];
            trigger.value = b64string
            source.change.emit();
            // also update matplotlib image data
        }

        function error_handler(evt) {
            if(evt.target.error.name == "NotReadableError") {
                alert("Can't read file!");
            }
        }

        var input = document.createElement('input');
        input.setAttribute('type', 'file');
        input.setAttribute('accept', 'image/*')
        input.onchange = function(){
            if (window.FileReader) { read_image(input.files[0]) }
            else { alert('FileReader is not supported in this browser');}
        }
        input.click();
        """
        #text input to pass along image data
        def update(attr, old, new):
            self.img_data = loadImage(new)
            height, width = self.img_data.shape[:2]
            adjust_plot(self.plot, height, width)
            self.img_url = new;

        textIn = TextInput(value="default")  
        textIn.on_change('value', update)

        callback = CustomJS(args=dict(source = self.source, xmax = self.xmax, ymax = self.ymax, trigger = textIn), 
                            code = __code__ )
        button = Button(label="Upload Image...", callback = callback)
        
        
        
        self.plot.image_url(url='url', x = 0, y = 0, w='xdim', h='ydim', source = self.source)

        init(self.plot, self.xmax, self.ymax, self.offset)
    
        return column(button, self.plot)



