import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04037, -0.00975).lineTo(0.0545, -0.00124).lineTo(0.0545, -0.00975).lineTo(0.04037, -0.00975).close()
solid=wp_sketch0.add(loop0).extrude(-0.008644574586626803)
