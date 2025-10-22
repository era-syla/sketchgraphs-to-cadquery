import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.005, 0.22314).lineTo(-0.005, 0.14514).lineTo(-0.02998, 0.14514).lineTo(-0.02998, 0.23514).lineTo(-0.0125, 0.23514).lineTo(-0.0125, 0.22314).lineTo(-0.005, 0.22314).close()
solid=wp_sketch0.add(loop0).extrude(0.26601710025295766)
