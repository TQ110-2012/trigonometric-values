import math
import random

angle = random.uniform(0, 360)  

radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print(f"Angle: {angle:.2f} degrees")
print(f"Sine: {sin_value:.4f}")
print(f"Cosine: {cos_value:.4f}")
print(f"Tangent: {tan_value:.4f}")