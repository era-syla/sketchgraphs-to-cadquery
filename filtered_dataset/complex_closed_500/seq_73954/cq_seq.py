import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0235, 0.0065).lineTo(0.0235, 0.0035).lineTo(0.0255, 0.0015).lineTo(0.0365, 0.0015).lineTo(0.0385, 0.0035).lineTo(0.0385, 0.0065).threePointArc((0.03821, 0.00721), (0.0375, 0.0075)).lineTo(0.0245, 0.0075).threePointArc((0.02379, 0.00721), (0.0235, 0.0065)).close()
solid=wp_sketch0.add(loop0).extrude(0.026137675146473117)
