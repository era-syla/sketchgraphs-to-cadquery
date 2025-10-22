import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00635, 0.0).lineTo(0.06985, 0.0).lineTo(0.06985, -0.00635).threePointArc((0.06799, -0.01084), (0.0635, -0.0127)).lineTo(0.0127, -0.0127).threePointArc((0.00821, -0.01084), (0.00635, -0.00635)).lineTo(0.00635, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.045219035684389834)
