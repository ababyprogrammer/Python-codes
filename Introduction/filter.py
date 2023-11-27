import math
import sys

from PIL import Image, ImageFilter

# Ensure correct using
if len(sys.argv) != 2:
    sys.exit("Usage: python filter.py filename")

# Open Image
image = Image.open(sys.srgv[1]).convert("RGB")

# Filter image according to edge delection kernel
filtered = image.filter(ImageFilter.Kernel(
    size= (5, 5),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))

# Show resulting image
filtered.show()