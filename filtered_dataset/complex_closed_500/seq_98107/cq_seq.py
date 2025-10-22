import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02735, 0.01354).lineTo(-0.02216, 0.01354).lineTo(-0.02216, -0.04543).lineTo(-0.02735, -0.04543).lineTo(-0.02735, 0.01354).close()
solid=wp_sketch0.add(loop0).extrude(-0.14874088812191483)
