import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0764, 0.01303).lineTo(0.17998, 0.01303).lineTo(0.17998, -0.01461).lineTo(0.0764, -0.01461).lineTo(0.0764, 0.01303).close()
solid=wp_sketch0.add(loop0).extrude(-0.06152335960546161)
