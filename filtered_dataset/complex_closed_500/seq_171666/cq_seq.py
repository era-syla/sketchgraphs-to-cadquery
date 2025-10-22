import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.00363).lineTo(0.00312, 0.00635).lineTo(0.00312, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.00363).close()
solid=wp_sketch0.add(loop0).extrude(0.013886191921125845)
