weight = int(input())
height = int(input())
weight2 = weight / 2.20462
height2 = height * 0.0254
total = round(weight2 / (height2 ** 2), 2)
print(total)