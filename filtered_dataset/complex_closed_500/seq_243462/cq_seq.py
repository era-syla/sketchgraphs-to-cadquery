import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06014, 0.05715).lineTo(-0.04109, 0.05715).lineTo(-0.04109, 0.0).lineTo(-0.06014, 0.0).lineTo(-0.06014, 0.05715).close()
solid=wp_sketch0.add(loop0).extrude(-0.030273993314904053)
