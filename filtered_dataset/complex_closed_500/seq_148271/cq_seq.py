import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.049, 0.0).threePointArc((0.04971, 0.00029), (0.05, 0.001)).lineTo(0.05, 0.0015).threePointArc((0.04971, 0.00221), (0.049, 0.0025)).lineTo(0.0075, 0.0025).threePointArc((0.00396, 0.00396), (0.0025, 0.0075)).lineTo(0.0025, 0.049).threePointArc((0.00221, 0.04971), (0.0015, 0.05)).lineTo(0.001, 0.05).threePointArc((0.00029, 0.04971), (-0.0, 0.049)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.13724695341251486)
