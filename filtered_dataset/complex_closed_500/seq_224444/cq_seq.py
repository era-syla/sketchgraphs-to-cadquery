import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.042, 0.0).lineTo(0.0435, 0.0).lineTo(0.0435, 0.027).lineTo(0.035, 0.027).lineTo(0.035, 0.015).lineTo(-0.014, 0.015).lineTo(-0.014, 0.027).lineTo(-0.042, 0.027).lineTo(-0.042, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.035808130011985795)
