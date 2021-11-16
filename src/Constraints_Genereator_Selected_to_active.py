import bpy
# The script works in Pose Mode\Edit Mode 
#  with 1 to N selected bones for which a 
#   constraint will be created and one 
#    active bone to which the bones will be 
#     referenced in the settings of the created 
#      constraint.

# context
original_mode = bpy.context.area.type
# active_bone_name gets the name of the active bone
active_bone_name = bpy.context.active_bone.name
# active_bone_name gets the name of the active armature
active_armature = bpy.context.active_object.name

# script saves the current mod
#  if bones were selected 
#   before creating the Constraint, 
#    Pose Mode will be enabled, 
#     the script will work and return the saved mod
#      it won't work without selected bones
cMode = bpy.context.object.mode
bpy.ops.object.mode_set(mode='POSE')

# goes sequentially through all of the selected bones
for bone in bpy.context.selected_pose_bones:

    # check that among the selected bones there is no active
    if bone.name != active_bone_name:

        # create constraint
        # const - constraint controller
        const = bone.constraints.new(type='COPY_TRANSFORMS')
        
        # preferences of the constraint
        const.target = bpy.data.objects[active_armature] # target is active armature
        const.subtarget = active_bone_name # the last selected bone (is active) will become the controlling one in Constraint
        const.mix_mode = 'REPLACE' # you can change it to 'AFTER' or 'BEFORE' or 'REPLACE'(by default)
        const.target_space = 'LOCAL_WITH_PARENT' # you can chage it to 'LOCAL_WITH_PARENT' or 'POSE' or 'LOCAL' or 'CUSTOM' or 'WORLD' (by default)
        const.owner_space = 'LOCAL_WITH_PARENT' # the same options as in the point above ^^^
        const.influence = 1.0 # a fractional number from 0 to 1

# back to the saved mode
bpy.ops.object.mode_set(mode=cMode)