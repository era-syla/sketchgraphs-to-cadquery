import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.027, 0.013).lineTo(0.027, 0.013).lineTo(0.027, -0.013).lineTo(-0.027, -0.013).lineTo(-0.027, 0.013).close()
solid=wp_sketch0.add(loop0).extrude(-0.1115954957038871)
