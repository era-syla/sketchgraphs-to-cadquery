import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01467, 0.03124).lineTo(0.01467, 0.03886).lineTo(0.01693, 0.03886).threePointArc((0.01748, 0.03866), (0.01777, 0.03816)).lineTo(0.01899, 0.03124).lineTo(0.01467, 0.03124).close()
solid=wp_sketch0.add(loop0).extrude(-0.008629014288629768)
