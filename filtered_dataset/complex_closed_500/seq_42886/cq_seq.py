import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02, 0.01075).lineTo(-0.005, 0.01075).lineTo(-0.005, 0.01475).lineTo(0.02, 0.01475).lineTo(0.02, 0.01075).close()
solid=wp_sketch0.add(loop0).extrude(0.04724203489927192)
