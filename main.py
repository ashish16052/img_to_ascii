from PIL import Image

# 1. image > bytes
img = Image.open("image.png")
img_data = list(img.getdata())


# 2. bytes > pixel grid

# 3. pixel grid -> ascii grid
