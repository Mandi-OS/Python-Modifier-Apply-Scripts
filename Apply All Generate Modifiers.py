import bpy

def apply_all_generate_modifiers(obj):
        # Apply the Array modifier
    if obj.modifiers.get('Array') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Array')
        # Apply the Bevel modifier
    if obj.modifiers.get('Bevel') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Bevel')
         # Apply the Boolean modifier
    if obj.modifiers.get('Boolean') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Boolean')
         # Apply the Build modifier
    if obj.modifiers.get('Build') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Build')
         # Apply the Decimate modifier
    if obj.modifiers.get('Decimate') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Decimate')
         # Apply the EdgeSplit modifier
    if obj.modifiers.get('EdgeSplit') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='EdgeSplit')
         # Apply the GeometryNodes modifier
    if obj.modifiers.get('GeometryNodes') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='GeometryNodes')
         # Apply the Mask modifier
    if obj.modifiers.get('Mask') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Mask')
         # Apply the Mirror modifier
    if obj.modifiers.get('Mirror') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Mirror')
         # Apply the Multires modifier
    if obj.modifiers.get('Multires') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Multires')
         # Apply the Remesh modifier
    if obj.modifiers.get('Remesh') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Remesh')
         # Apply the Screw modifier
    if obj.modifiers.get('Screw') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Screw')
         # Apply the Skin modifier
    if obj.modifiers.get('Skin') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Skin')
         # Apply the Solididy modifier
    if obj.modifiers.get('Solididy') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Solididy')
         # Apply the Subdivision modifier
    if obj.modifiers.get('Subdivision') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Subdivision')
         # Apply the Triangulate modifier
    if obj.modifiers.get('Triangulate') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Triangulate')
         # Apply the Volume to Mesh modifier
    if obj.modifiers.get('Volume to Mesh') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Volume to Mesh')
         # Apply the Weld modifier
    if obj.modifiers.get('Weld') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Weld')
         # Apply the Wireframe modifier
    if obj.modifiers.get('Wireframe') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Wireframe')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            apply_all_generate_modifiers(obj)

if __name__ == "__main__":
    main()