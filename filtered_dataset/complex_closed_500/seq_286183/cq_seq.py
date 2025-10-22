import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00246, -0.015).lineTo(-0.05754, -0.015).lineTo(-0.05754, 0.035).lineTo(0.00246, 0.035).lineTo(0.00246, -0.015).close()
solid=wp_sketch0.add(loop0).extrude(0.015633511378746006)
