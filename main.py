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
cpx_factor = 10 # compression factor
pixels = [
    img_data[i * width : (i + 1) * width : cpx_factor]
    for i in range(0, height, cpx_factor)
]

# 3. pixel grid -> ascii grid
ascii = ".:+*#@%0"  # 8 characters arranged in increasing order of density (brightness)
with open("output.txt", "+w") as f:
    for px_row in pixels:
        for r, g, b in px_row:
            binary_index = (r > 128, g > 128, b > 128)
            # R, G, B index ascii
            # 0  0  0     0     .
            # 0  0  1     1     :
            # 0  1  0     2     +
            # 0  1  1     3     *
            # 1  0  0     4     #
            # 1  0  1     5     @
            # 1  1  0     6     %
            # 1  1  1     7     0
            index = int("".join(str(int(x)) for x in binary_index), 2)
            f.write(f"{ascii[index]} ")
        f.write("\n")