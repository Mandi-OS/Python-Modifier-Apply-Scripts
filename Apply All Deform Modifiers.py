import bpy

def apply_all_deform_modifiers(obj):
        # Apply the Armature modifier
    if obj.modifiers.get('Armature') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Armature')
        # Apply the Cast modifier
    if obj.modifiers.get('Cast') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Cast')
         # Apply the Curve modifier
    if obj.modifiers.get('Curve') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Curve')
         # Apply the Displace modifier
    if obj.modifiers.get('Displace') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Displace')
         # Apply the Hook modifier
    if obj.modifiers.get('Hook') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Hook')
         # Apply LaplacianDeform modifier
    if obj.modifiers.get('LaplacianDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='LaplacianDeform')
         # Apply the Lattice modifier
    if obj.modifiers.get('Lattice') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Lattice')
         # Apply the MeshDeform modifier
    if obj.modifiers.get('MeshDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='MeshDeform')
         # Apply the Shrinkwrap modifier
    if obj.modifiers.get('Shrinkwrap') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Shrinkwrap')
         # Apply the SimpleDeform modifier
    if obj.modifiers.get('SimpleDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='SimpleDeform')
         # Apply the Smooth modifier
    if obj.modifiers.get('Smooth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Smooth')
         # Apply the CorrectiveSmooth modifier
    if obj.modifiers.get('CorrectiveSmooth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='CorrectiveSmooth')
         # Apply the LaplacianSmooth modifier
    if obj.modifiers.get('LaplacianSmooth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='LaplacianSmooth')
         # Apply the SurfaceDeform modifier
    if obj.modifiers.get('SurfaceDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='SurfaceDeform')
         # Apply the Warp modifier
    if obj.modifiers.get('Warp') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Warp')
         # Apply the Wave modifier
    if obj.modifiers.get('Wave') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Wave')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            apply_all_deform_modifiers(obj)

if __name__ == "__main__":
    main()