import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02, -0.007).lineTo(0.02, -0.007).lineTo(0.02, -0.011).lineTo(-0.02, -0.011).lineTo(-0.02, -0.007).close()
solid=wp_sketch0.add(loop0).extrude(-0.012652662381115327)
