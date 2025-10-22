import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.011).lineTo(-0.0, 0.013).lineTo(0.013, 0.013).lineTo(0.013, 0.011).lineTo(0.0, 0.011).close()
solid=wp_sketch0.add(loop0).extrude(0.03511024527143329)
