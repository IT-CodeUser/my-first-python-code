import bpy
import random

# Clear existing mesh objects in the scene to start fresh
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# The Art Loop: Generate 50 unique rocks instantly
for i in range(50):
    # 1. Logic: Calculate a random position on the ground
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = 0 
    
    # 2. Art: Create a basic mathematical sphere as our rock base
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=1, location=(x, y, z))
    rock = bpy.context.active_object
    
    # 3. Art: Give it random proportions so they don't look identical
    scale_x = random.uniform(0.5, 1.5)
    scale_y = random.uniform(0.5, 1.5)
    scale_z = random.uniform(0.2, 1.0) # Flatter on the Z-axis like real rocks
    rock.scale = (scale_x, scale_y, scale_z)
    
    # 4. Logic: Rotate it randomly so the textures don't align perfectly
    rock.rotation_euler = (
        random.uniform(0, 6.28), 
        random.uniform(0, 6.28), 
        random.uniform(0, 6.28)
    )