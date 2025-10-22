import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.011, 0.011).lineTo(0.011, 0.011).lineTo(0.011, -0.011).lineTo(-0.011, -0.011).lineTo(-0.011, 0.011).close()
solid=wp_sketch0.add(loop0).extrude(0.021672817490273527)
