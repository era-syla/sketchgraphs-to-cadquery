import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.004, 0.025).lineTo(-0.004, 0.025).threePointArc((-0.00541, 0.02441), (-0.006, 0.023)).lineTo(-0.006, 0.013).threePointArc((-0.00541, 0.01159), (-0.004, 0.011)).lineTo(0.004, 0.011).threePointArc((0.00541, 0.01159), (0.006, 0.013)).lineTo(0.006, 0.023).threePointArc((0.00541, 0.02441), (0.004, 0.025)).close()
solid=wp_sketch0.add(loop0).extrude(0.01212521440050267)
