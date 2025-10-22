import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00035, 0.04653).lineTo(0.00531, 0.04653).lineTo(0.00531, 0.05071).lineTo(0.00035, 0.05071).lineTo(0.00035, 0.04653).close()
solid=wp_sketch0.add(loop0).extrude(0.005452765454039609)
