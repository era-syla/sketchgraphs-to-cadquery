import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-2.7, -0.0).lineTo(5.3, -0.0).lineTo(5.3, -5.0).lineTo(-2.7, -5.0).lineTo(-2.7, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(15.618792626501218)
