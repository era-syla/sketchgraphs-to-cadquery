import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04, 0.015).lineTo(0.04, 0.015).threePointArc((0.04707, 0.01207), (0.05, 0.005)).lineTo(0.05, -0.005).threePointArc((0.04707, -0.01207), (0.04, -0.015)).lineTo(-0.04, -0.015).threePointArc((-0.04707, -0.01207), (-0.05, -0.005)).lineTo(-0.05, 0.005).threePointArc((-0.04707, 0.01207), (-0.04, 0.015)).close()
solid=wp_sketch0.add(loop0).extrude(0.27497725811776075)
