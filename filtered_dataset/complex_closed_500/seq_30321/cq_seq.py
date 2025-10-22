import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00355, 0.0).lineTo(0.08535, 0.0).threePointArc((0.09366, 0.00318), (0.08535, 0.00635)).lineTo(0.00355, 0.00635).threePointArc((-0.00476, 0.00318), (0.00355, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.17003818547696486)
