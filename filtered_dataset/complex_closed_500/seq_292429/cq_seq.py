import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.08, 0.0).lineTo(0.08, -0.05).lineTo(0.0, -0.05).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.0863812953969557)
