import bpy
import math

# Assume you have these coordinates
right_shoulder_coords = (0.38511741161346436, 0.4334025979042053, -0.3169334828853607)
right_elbow_coords = (0.33880549669265747, 0.711230993270874, -0.23487141728401184)

# Calculate the direction vector from shoulder to elbow
x = (right_elbow_coords[0] - right_shoulder_coords[0])/2
y = (right_elbow_coords[1] - right_shoulder_coords[1])/2
z = (right_elbow_coords[2] - right_shoulder_coords[2])/2

coord = (x,y,z)

print(coord)


