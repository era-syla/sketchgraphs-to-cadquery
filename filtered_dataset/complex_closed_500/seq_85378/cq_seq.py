import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01441, 0.011).lineTo(0.04041, 0.011).threePointArc((0.04076, 0.01085), (0.04091, 0.0105)).lineTo(0.04091, -0.0105).threePointArc((0.04076, -0.01085), (0.04041, -0.011)).lineTo(0.01441, -0.011).threePointArc((0.01406, -0.01085), (0.01391, -0.0105)).lineTo(0.01391, 0.0105).threePointArc((0.01406, 0.01085), (0.01441, 0.011)).close()
solid=wp_sketch0.add(loop0).extrude(-0.06393894174657971)
