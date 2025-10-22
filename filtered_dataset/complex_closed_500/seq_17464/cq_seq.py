import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.025, 0.02).lineTo(0.025, 0.02).lineTo(0.025, -0.02).lineTo(-0.025, -0.02).lineTo(-0.025, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(-0.026752604865820095)
