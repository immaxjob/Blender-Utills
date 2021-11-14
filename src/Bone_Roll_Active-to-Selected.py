import bpy

# Сохраняю оригинальный мод
# Saving the original mod
original_mode = bpy.context.area.type

# определяю текущий мод, меняю на EDIT MODE
# detect the current mod, change to EDIT MODE
cMode = bpy.context.object.mode
bpy.ops.object.mode_set(mode='EDIT')

# Roll активной кости
# Roll of the active bone
ab = bpy.context.active_bone.roll

# Замена Roll выбранной кости на Roll активной кости
# Replacing the Roll of the selected bone with the Roll of the active bone
for bone in bpy.context.selected_bones:
    bone.roll = ab
        
# Возвращаю в исходный мод
# Returning to the original mod
bpy.ops.object.mode_set(mode=cMode)