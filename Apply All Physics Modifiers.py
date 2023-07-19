import bpy

def apply_all_physics_modifiers(obj):
        # Apply the Cloth modifier
    if obj.modifiers.get('Cloth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Cloth')
        # Apply the Collision modifier
    if obj.modifiers.get('Collision') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Collision')
         # Apply the Dynamic Paint modifier
    if obj.modifiers.get('Dynamic Paint') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Dynamic Paint')
         # Apply the Explode modifier
    if obj.modifiers.get('Explode') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Explode')
         # Apply the Fluid modifier
    if obj.modifiers.get('Fluid') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Fluid')
         # Apply the Ocean modifier
    if obj.modifiers.get('Ocean') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Ocean')
         # Apply the ParticleInstance modifier
    if obj.modifiers.get('ParticleInstance') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='ParticleInstance')
         # Apply the ParticleSystem modifier
    if obj.modifiers.get('ParticleSystem') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='ParticleSystem')
         # Apply the Softbody modifier
    if obj.modifiers.get('Softbody') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier='Softbody')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            apply_all_physics_modifiers(obj)

if __name__ == "__main__":
    main()