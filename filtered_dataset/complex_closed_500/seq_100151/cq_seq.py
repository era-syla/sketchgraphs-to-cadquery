import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.06168).lineTo(-0.045, 0.015).lineTo(-0.035, 0.015).lineTo(-0.02, 0.04668).lineTo(-0.02, 0.06168).close()
solid=wp_sketch0.add(loop0).extrude(0.0249574212614863)
