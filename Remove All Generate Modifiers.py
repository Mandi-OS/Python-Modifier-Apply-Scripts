import bpy

def remove_all_generate_modifiers(obj):
        # Remove the Array modifier
    if obj.modifiers.get('Array') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Array')
        # Remove the Bevel modifier
    if obj.modifiers.get('Bevel') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Bevel')
         # Remove the Boolean modifier
    if obj.modifiers.get('Boolean') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Boolean')
         # Remove the Build modifier
    if obj.modifiers.get('Build') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Build')
         # Remove the Decimate modifier
    if obj.modifiers.get('Decimate') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Decimate')
         # Remove the EdgeSplit modifier
    if obj.modifiers.get('EdgeSplit') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='EdgeSplit')
         # Remove the GeometryNodes modifier
    if obj.modifiers.get('GeometryNodes') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='GeometryNodes')
         # Remove the Mask modifier
    if obj.modifiers.get('Mask') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Mask')
         # Remove the Mirror modifier
    if obj.modifiers.get('Mirror') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Mirror')
         # Remove the Multires modifier
    if obj.modifiers.get('Multires') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Multires')
         # Remove the Remesh modifier
    if obj.modifiers.get('Remesh') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Remesh')
         # Remove the Screw modifier
    if obj.modifiers.get('Screw') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Screw')
         # Remove the Skin modifier
    if obj.modifiers.get('Skin') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Skin')
         # Remove the Solididy modifier
    if obj.modifiers.get('Solididy') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Solididy')
         # Remove the Subdivision modifier
    if obj.modifiers.get('Subdivision') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Subdivision')
         # Remove the Triangulate modifier
    if obj.modifiers.get('Triangulate') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Triangulate')
         # Remove the Volume to Mesh modifier
    if obj.modifiers.get('Volume to Mesh') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Volume to Mesh')
         # Remove the Weld modifier
    if obj.modifiers.get('Weld') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Weld')
         # Remove the Wireframe modifier
    if obj.modifiers.get('Wireframe') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Wireframe')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            remove_all_generate_modifiers(obj)

if __name__ == "__main__":
    main()