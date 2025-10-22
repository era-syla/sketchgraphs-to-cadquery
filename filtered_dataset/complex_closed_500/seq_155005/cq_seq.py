import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01141, -0.03572).threePointArc((0.0, -0.0375), (0.01141, -0.03572)).lineTo(0.06359, -0.01905).threePointArc((0.0775, 0.0), (0.06359, 0.01905)).lineTo(0.01141, 0.03572).threePointArc((0.0, 0.0375), (-0.01141, 0.03572)).lineTo(-0.06359, 0.01905).threePointArc((-0.0775, -0.0), (-0.06359, -0.01905)).lineTo(-0.01141, -0.03572).close()
solid=wp_sketch0.add(loop0).extrude(-0.32261998250655566)
