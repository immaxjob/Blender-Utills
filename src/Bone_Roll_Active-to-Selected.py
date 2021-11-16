import bpy

# Saving the original mod
original_mode = bpy.context.area.type

# detect the current mod, change to EDIT MODE
cMode = bpy.context.object.mode
bpy.ops.object.mode_set(mode='EDIT')

# Roll of the active bone
ab = bpy.context.active_bone.roll

# Replacing the Roll of the selected bone with the Roll of the active bone
for bone in bpy.context.selected_bones:
    bone.roll = ab
        
# Returning to the original mod
bpy.ops.object.mode_set(mode=cMode)