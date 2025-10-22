import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0175, -0.015).lineTo(-0.0175, -0.015).threePointArc((-0.02104, -0.01354), (-0.0225, -0.01)).lineTo(-0.0225, 0.01).threePointArc((-0.02104, 0.01354), (-0.0175, 0.015)).lineTo(0.0175, 0.015).threePointArc((0.02104, 0.01354), (0.0225, 0.01)).lineTo(0.0225, -0.01).threePointArc((0.02104, -0.01354), (0.0175, -0.015)).close()
solid=wp_sketch0.add(loop0).extrude(-0.12341016637649616)
