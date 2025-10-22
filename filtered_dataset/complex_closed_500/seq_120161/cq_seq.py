import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0612, 0.02553).lineTo(0.0747, 0.02553).lineTo(0.0747, 0.05953).lineTo(0.0612, 0.05953).lineTo(0.0612, 0.02553).close()
solid=wp_sketch0.add(loop0).extrude(-0.007373530280256393)
