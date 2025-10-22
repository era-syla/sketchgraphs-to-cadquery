import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02856, 0.0).lineTo(0.03702, -0.00562).lineTo(0.02792, -0.01014).lineTo(0.02856, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0027960660800391045)
