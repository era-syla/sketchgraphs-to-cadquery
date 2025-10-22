import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.15257, 0.09239).lineTo(0.15223, 0.09239).lineTo(0.15223, -0.13621).lineTo(-0.15257, -0.13621).lineTo(-0.15257, 0.09239).close()
solid=wp_sketch0.add(loop0).extrude(-0.1221335639221563)
