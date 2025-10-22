import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.15266, -0.03404).lineTo(0.15234, -0.03404).lineTo(0.15234, -0.01404).lineTo(-0.15266, 0.03596).lineTo(-0.15266, -0.03404).close()
solid=wp_sketch0.add(loop0).extrude(0.4472089550310432)
