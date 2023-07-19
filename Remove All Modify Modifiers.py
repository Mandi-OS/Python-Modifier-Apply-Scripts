import bpy

def remove_all_modify_modifiers(obj):
        # Remove the DataTransfer modifier
    if obj.modifiers.get('DataTransfer') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='DataTransfer')
        # Remove the MeshCache modifier
    if obj.modifiers.get('MeshCache') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='MeshCache')
         # Remove the MeshSequenceCache modifier
    if obj.modifiers.get('MeshSequenceCache') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='MeshSequenceCache')
         # Remove the NormalEdit modifier
    if obj.modifiers.get('NormalEdit') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='NormalEdit')
         # Remove the WeightedNormal modifier
    if obj.modifiers.get('WeightedNormal') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='WeightedNormal')
         # Remove the UVProject modifier
    if obj.modifiers.get('UVProject') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='UVProject')
         # Remove the UVWarp modifier
    if obj.modifiers.get('UVWarp') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='UVWarp')
         # Remove the VertexWeightEdit modifier
    if obj.modifiers.get('VertexWeightEdit') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='VertexWeightEdit')
         # Remove the VertexWeightMix modifier
    if obj.modifiers.get('VertexWeightMix') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='VertexWeightMix')
         # Remove the VertexWeightProximity modifier
    if obj.modifiers.get('VertexWeightProximity') is not None:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier='VertexWeightProximity')

def main():
    # Check if there are selected objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            remove_all_modify_modifiers(obj)

if __name__ == "__main__":
    main()