import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00987, 0.00791).lineTo(-0.00987, 0.02302).lineTo(0.04728, 0.02302).lineTo(0.07052, 0.01818).lineTo(0.07052, 0.00791).lineTo(-0.00987, 0.00791).close()
solid=wp_sketch0.add(loop0).extrude(0.14987214422209882)
