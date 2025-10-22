import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.015, -0.00013).lineTo(-0.015, -0.00013).lineTo(-0.015, 0.00012).lineTo(0.015, 0.00012).lineTo(0.015, -0.00013).close()
solid=wp_sketch0.add(loop0).extrude(-0.07262458293805382)
