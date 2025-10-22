import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(2.3793, 0.08275).lineTo(1.2355, 0.08275).lineTo(1.2355, 0.06243).lineTo(2.3791, 0.06243).lineTo(2.3793, 0.08275).close()
solid=wp_sketch0.add(loop0).extrude(-1.5819471004657386)
