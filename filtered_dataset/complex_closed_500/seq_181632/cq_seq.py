import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.114, 0.0).lineTo(0.084, 0.0).lineTo(0.084, 0.005).lineTo(0.114, 0.005).lineTo(0.114, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.07422935525056186)
