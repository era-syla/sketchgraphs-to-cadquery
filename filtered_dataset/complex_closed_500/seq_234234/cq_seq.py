import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.004, 0.0).lineTo(-0.004, 0.0).lineTo(-0.004, 0.004).lineTo(0.004, 0.004).lineTo(0.004, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.007712660740908234)
