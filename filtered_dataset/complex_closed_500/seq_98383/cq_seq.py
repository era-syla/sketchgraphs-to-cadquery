import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00762, 0.00635).lineTo(0.00508, 0.00635).lineTo(0.00508, 0.00381).lineTo(0.00762, 0.00381).lineTo(0.00762, 0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.001883432803718032)
