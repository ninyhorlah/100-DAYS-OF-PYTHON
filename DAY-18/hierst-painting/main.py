import colorgram

colors = colorgram.extract("/Users/N.Akande/Desktop/tutorials/100-DAYS-OF-PYTHON/DAY-18/hierst-painting/image1.jpg", 20)
rgb = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_rgb = (r, g, b)
    rgb.append(new_rgb)

print(rgb)