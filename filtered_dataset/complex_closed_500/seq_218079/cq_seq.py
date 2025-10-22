import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.004, 0.016).lineTo(0.0, 0.016).lineTo(0.0, 0.012).lineTo(-0.004, 0.012).lineTo(-0.004, 0.016).close()
solid=wp_sketch0.add(loop0).extrude(9.212195083387443e-05)
