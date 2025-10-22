import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0735, 0.15).lineTo(0.0735, 0.00811).threePointArc((0.07304, 0.00581), (0.07174, 0.00386)).lineTo(0.06988, 0.002).lineTo(0.06, 0.002).lineTo(0.06, 0.0).lineTo(0.07, 0.0).lineTo(0.0728, 0.0028).threePointArc((0.07443, 0.00524), (0.075, 0.00811)).lineTo(0.075, 0.15).lineTo(0.0735, 0.15).close()
solid=wp_sketch0.add(loop0).extrude(0.3834331443834665)
