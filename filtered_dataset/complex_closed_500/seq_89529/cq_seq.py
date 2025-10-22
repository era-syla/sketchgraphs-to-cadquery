import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.21857, -0.30006).lineTo(-0.21857, -0.30006).lineTo(-0.21857, 0.30006).lineTo(0.21857, 0.30006).lineTo(0.21857, -0.30006).close()
solid=wp_sketch0.add(loop0).extrude(-1.1449759761268743)
