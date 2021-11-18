import bpy

# cMode saves the current mode. Mode changes to Pose Mode
cMode = bpy.context.object.mode
bpy.ops.object.mode_set(mode='POSE')

# For all selected bones in pose mode
for bone in bpy.context.selected_pose_bones:
    # Creating a list of all constraint on selected bones Copy location
    list_of_const = [ const for const in bone.constraints if const.type == 'CAMERA_SOLVER' or const.type == 'FOLLOW_TRACK' 
    or const.type == 'OBJECT_SOLVER' or const.type == 'COPY_LOCATION' or const.type == 'COPY_ROTATION' or const.type == 'COPY_SCALE' or const.type == 'COPY_TRANSFORMS' or const.type == 'LIMIT_DISTANCE' or const.type == 'LIMIT_LOCATION' 
    or const.type == 'LIMIT_ROTATION' or const.type == 'LIMIT_SCALE' or const.type == 'MAINTAIN_VOLUME' or const.type == 'TRANSFORM' or const.type == 'TRANSFORM_CACHE' or const.type == 'CLAMP_TO' or const.type == 'DAMPED_TRACK' or const.type == 'IK' 
    or const.type == 'LOCKED_TRACK' or const.type == 'SPLINE_IK' or const.type == 'STRETCH_TO' or const.type == 'TRACK_TO' or const.type == 'ACTION' or const.type == 'ARMATURE' or const.type == 'CHILD_OF' or const.type == 'FLOOR' or const.type == 'FOLLOW_PATH' 
	or const.type == 'PIVOT' or const.type == 'SHRINKWRAP']
    
	# Remove all constraints in list
    for const in list_of_const:
        bone.constraints.remove(const)

# Return saved mode
bpy.ops.object.mode_set(mode=cMode)