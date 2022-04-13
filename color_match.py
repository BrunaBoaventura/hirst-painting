import colorgram

colors = colorgram.extract('image.jpg', 9)

rgb_list = []
for color in range(9):
    color_details = colors[color]
    rgb_list.append(tuple(color_details.rgb))

print(rgb_list)
