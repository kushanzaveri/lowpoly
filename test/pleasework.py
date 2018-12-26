import base64
import io
from imageio import imread
import matplotlib.pyplot as plt

filename = "lake.jpg"
with open(filename, "rb") as fid:
    data = fid.read()

b64_bytes = base64.b64encode(data)
b64_string = b64_bytes.decode()

# reconstruct image as an numpy array
img = imread(io.BytesIO(base64.b64decode(b64_string)))

# show image
plt.figure()
plt.imshow(img, cmap="gray")

plt.show()