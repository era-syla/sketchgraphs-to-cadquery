import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.09, -0.015).lineTo(-0.09, -0.01).lineTo(0.09, -0.01).lineTo(0.09, -0.015).lineTo(0.08671, -0.015).threePointArc((0.07823, -0.01689), (0.07134, -0.0222)).lineTo(0.01984, -0.084).threePointArc((0.01124, -0.09064), (0.00063, -0.093)).lineTo(-0.00063, -0.093).threePointArc((-0.01124, -0.09064), (-0.01984, -0.084)).lineTo(-0.07134, -0.0222).threePointArc((-0.07823, -0.01689), (-0.08671, -0.015)).lineTo(-0.09, -0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.3791939555231836)
