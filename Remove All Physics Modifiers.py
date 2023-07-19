import bpy

def remove_all_physics_modifiers(obj):
        # Remove the Cloth modifier
    if obj.modifiers.get('Cloth') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Cloth')
        # Remove the Collision modifier
    if obj.modifiers.get('Collision') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Collision')
         # Remove the Dynamic Paint modifier
    if obj.modifiers.get('Dynamic Paint') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Dynamic Paint')
         # Remove the Explode modifier
    if obj.modifiers.get('Explode') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Explode')
         # Remove the Fluid modifier
    if obj.modifiers.get('Fluid') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Fluid')
         # Remove the Ocean modifier
    if obj.modifiers.get('Ocean') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Ocean')
         # Remove the ParticleInstance modifier
    if obj.modifiers.get('ParticleInstance') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='ParticleInstance')
         # Remove the ParticleSystem modifier
    if obj.modifiers.get('ParticleSystem') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='ParticleSystem')
         # Remove the Softbody modifier
    if obj.modifiers.get('Softbody') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='Softbody')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            remove_all_physics_modifiers(obj)

if __name__ == "__main__":
    main()