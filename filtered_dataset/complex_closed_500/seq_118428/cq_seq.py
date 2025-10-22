import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0535, 0.0).lineTo(0.0695, 0.0).lineTo(0.0695, -0.025).lineTo(0.0535, -0.025).lineTo(0.0535, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.02595073894143294)
