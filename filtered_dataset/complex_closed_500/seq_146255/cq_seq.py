import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.8, 2.36).lineTo(-1.5, 2.36).lineTo(-1.5, 0.0).lineTo(-0.8, 0.0).lineTo(-0.8, 2.36).close()
solid=wp_sketch0.add(loop0).extrude(-1.1292986597245458)
