import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00791, 0.02542).lineTo(-0.04391, 0.02542).lineTo(-0.04391, -0.03458).lineTo(-0.00791, -0.03458).lineTo(-0.00791, 0.02542).close()
solid=wp_sketch0.add(loop0).extrude(0.004762369204294998)
