from image_match.goldberg import ImageSignature
gis = ImageSignature()
a = gis.generate_signature('1.jpg')
b = gis.generate_signature('images/23949512.jpg')
diff = gis.normalized_distance(a, b)
print(diff)