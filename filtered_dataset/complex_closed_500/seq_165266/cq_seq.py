import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02014, 0.02014).lineTo(-0.02014, 0.02014).lineTo(-0.02014, -0.02014).lineTo(0.02014, -0.02014).lineTo(0.02014, 0.02014).close()
solid=wp_sketch0.add(loop0).extrude(-0.11388050639397218)
