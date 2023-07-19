import bpy

def remove_all_deform_modifiers(obj):
        # Remove the Armature modifier
    if obj.modifiers.get('Armature') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Armature')
        # Remove the Cast modifier
    if obj.modifiers.get('Cast') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Cast')
         # Remove the Curve modifier
    if obj.modifiers.get('Curve') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Curve')
         # Remove the Displace modifier
    if obj.modifiers.get('Displace') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Displace')
         # Remove the Hook modifier
    if obj.modifiers.get('Hook') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Hook')
         # Remove LaplacianDeform modifier
    if obj.modifiers.get('LaplacianDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='LaplacianDeform')
         # Remove the Lattice modifier
    if obj.modifiers.get('Lattice') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Lattice')
         # Remove the MeshDeform modifier
    if obj.modifiers.get('MeshDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='MeshDeform')
         # Remove the Shrinkwrap modifier
    if obj.modifiers.get('Shrinkwrap') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Shrinkwrap')
         # Remove the SimpleDeform modifier
    if obj.modifiers.get('SimpleDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='SimpleDeform')
         # Remove the Smooth modifier
    if obj.modifiers.get('Smooth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Smooth')
         # Remove the CorrectiveSmooth modifier
    if obj.modifiers.get('CorrectiveSmooth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='CorrectiveSmooth')
         # Remove the LaplacianSmooth modifier
    if obj.modifiers.get('LaplacianSmooth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='LaplacianSmooth')
         # Remove the SurfaceDeform modifier
    if obj.modifiers.get('SurfaceDeform') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='SurfaceDeform')
         # Remove the Warp modifier
    if obj.modifiers.get('Warp') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Warp')
         # Remove the Wave modifier
    if obj.modifiers.get('Wave') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Wave')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            remove_all_deform_modifiers(obj)

if __name__ == "__main__":
    main()