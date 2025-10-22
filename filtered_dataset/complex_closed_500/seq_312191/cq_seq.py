import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.049, 0.0).lineTo(-0.044, 0.0).lineTo(-0.044, 0.01064).lineTo(-0.049, 0.01064).lineTo(-0.049, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.009158097504102155)
