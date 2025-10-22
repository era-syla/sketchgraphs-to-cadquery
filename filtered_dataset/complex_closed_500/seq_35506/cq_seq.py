import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01125, -0.0325).lineTo(-0.01125, -0.0325).threePointArc((-0.0139, -0.0314), (-0.015, -0.02875)).lineTo(-0.015, 0.02875).threePointArc((-0.0139, 0.0314), (-0.01125, 0.0325)).lineTo(0.01125, 0.0325).threePointArc((0.0139, 0.0314), (0.015, 0.02875)).lineTo(0.015, -0.02875).threePointArc((0.0139, -0.0314), (0.01125, -0.0325)).close()
solid=wp_sketch0.add(loop0).extrude(-0.04373369355674347)
