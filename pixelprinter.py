from PIL import Image
#im = Image.open("charmander.png")
im = Image.open("nyan.png")
#im = Image.open("pikachu.png")
pix = im.load()
rgb_im = im.convert('RGB')

# output = "charmander = ["
# for x in range(20):
# 	output = output + "["
# 	for y in range(20):
# 		r, g, b = rgb_im.getpixel((x, y))

# 		if r == 0 and g == 0 and b == 0:
# 			output = output + "b"
# 		elif r == 255 and g == 156 and b == 6:
# 			output = output + "o"
# 		elif r == 255 and g == 255 and b == 255:
# 			output = output + "w"
# 		elif r == 255 and g == 228 and b == 69:
# 			output = output + "y"
# 		elif r == 250 and g == 64 and b == 51:
# 			output = output + "r"
# 		else:
# 			output = output + "green"
# 		if y != 19:
# 			output = output + ","

# 	if x != 19:
# 		output = output + "], "
# 	else:
# 		output = output + "]]"

# output = "pikachu = ["
# for x in range(40):
# 	output = output + "["
# 	for y in range(40):
# 		r, g, b = rgb_im.getpixel((x, y))
# 		if r == 0 and g == 0 and b == 0:
# 			output += "b"
# 		elif r == 252 and g == 233 and b == 78:
# 			output += "y"
# 		elif r == 242 and g == 163 and b == 58:
# 			output += "o" #accent color
# 		elif r == 126 and g == 80 and b == 25:
# 			output += "br" #brown
# 		elif r == 235 and g == 50 and b == 35:
# 			output += "r"
# 		elif r == 255 and g == 255 and b == 255:
# 			output += "w"
# 		else:
# 			output += "g"
# 		if y != 39:
# 			output = output + ","

# 	if x != 39:
# 		output = output + "], "
# 	else:
# 		output = output + "]]"

output = "nyan = ["
for x in range(40):
	output = output + "["
	for y in range(40):
		r, g, b = rgb_im.getpixel((x, y))
		if r == 0 and g == 0 and b == 0:
			output += "b"
		elif r == 248 and g == 255 and b == 1:
			output += "y"
		elif r == 255 and g == 144 and b == 0:
			output += "o"
		elif r == 255 and g == 0 and b == 0:
			output += "r"
		elif r == 255 and g == 255 and b == 255:
			output += "w"
		elif r == 255 and g == 248 and b == 180:
			output += "y" #poptart yellow
		elif r == 255 and g == 179 and b == 243:
			output += "p" #poptart pink
		elif r == 237 and g == 13 and b == 254:
			output += "p" #poptart purple
		elif r == 136 and g == 131 and b == 138:
			output += "gr"
		elif r == 254 and g == 138 and b == 138:
			output += "r" #face blush
		elif r == 27 and g == 191 and b == 32:
			output += "g"
		elif r == 84 and g == 158 and b == 255:
			output += "cy"
		elif r == 0 and g == 50 and b == 103:
			output += "bl"
		elif r == 108 and g == 10 and b == 255:
			output += "p"
		else:
			output += "g"
		if y != 39:
			output = output + ","

	if x != 39:
		output = output + "], "
	else:
		output = output + "]]"



print(output)

