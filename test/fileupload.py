
from bokeh.io import output_file
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.models import CustomJS, Slider
from bokeh.models.widgets import Button
from bokeh.models import Range1d
from bokeh.layouts import row
import numpy as np
output_file("foo.html")

img_url = "face.jpg"

p = figure(plot_width=1024, plot_height=1024)
p.x_range = Range1d(0, 1024)
p.y_range = Range1d(-1024, 0)

ds = ColumnDataSource(data=dict(url=[img_url]))
# p.image_url(url='url', x=0, y=1024, w=1024, h=1024, source=ds, palette="Spectral11")
p.image_url(url='url', x=0, y = 0, h=1024, w=1024, source=ds)


callback = CustomJS(args=dict(source=ds), code= """

function load_handler(event) {
    var b64string = event.target.result;
    source.data['url'] = [b64string];
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
    if (window.FileReader) {
        console.log("Read File!");
        var reader = new FileReader();
        reader.onload = load_handler;
        reader.onerror = error_handler;
        reader.readAsDataURL(input.files[0])
    } else {
        alert('FileReader is not supported in this browser');
    }
}
input.click();

/*
var reader = new FileReader();
reader.readAsDataURL(filename);
console.log(reader.result);
data['url'] = [reader.result];
source.change.emit();
*/
/*
    var loc = window.location.pathname;
    var dir = loc.substring(0, loc.lastIndexOf('/'));
    console.log(dir);
    var data = source.data;
    console.log(data['url']);
    data['url'] = ["./lake.jpg"];
    source.change.emit();
*/

""")



button = Button(label="Upload File", button_type="success", callback = callback)



show(row(button,p))





'''
from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import figure, output_file, show

output_file("callback.html")

x = [x*0.005 for x in range(0, 200)]
y = x


source = ColumnDataSource(data=dict(x=x, y=y))
plot = figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var f = cb_obj.value
        var x = data['x']
        var y = data['y']
        for (var i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], f)
        }
        //source.change.emit();
    """)

slider = Slider(start=0.1, end=4, value=1, step=.1, title="power", callback=callback)

layout = column(slider, plot)

show(layout)

'''
