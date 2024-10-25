from PIL import Image

# 1. image > bytes
img = Image.open("image.png")
img_data = list(img.getdata())


# 2. bytes > pixel grid
# [
#     [(r,g,b), (r,g,b), (r,g,b)],
#     [(r,g,b), (r,g,b), (r,g,b)],
#     [(r,g,b), (r,g,b), (r,g,b)],
#     [(r,g,b), (r,g,b), (r,g,b)],
#     [(r,g,b), (r,g,b), (r,g,b)],
# ]
width, height = img.size
pixels = [
    img_data[i * width : (i + 1) * width ]
    for i in range(0, height)
]

# 3. pixel grid -> ascii grid
