import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0298, 0.04137).lineTo(-0.0298, 0.04137).lineTo(-0.0298, -0.04137).lineTo(0.0298, -0.04137).lineTo(0.0298, 0.04137).close()
solid=wp_sketch0.add(loop0).extrude(0.05185788149289169)
