import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0381, 0.01905).lineTo(-0.0381, 0.01905).threePointArc((-0.04259, 0.01719), (-0.04445, 0.0127)).lineTo(-0.04445, -0.0127).threePointArc((-0.04259, -0.01719), (-0.0381, -0.01905)).lineTo(0.0381, -0.01905).threePointArc((0.04259, -0.01719), (0.04445, -0.0127)).lineTo(0.04445, 0.0127).threePointArc((0.04259, 0.01719), (0.0381, 0.01905)).close()
solid=wp_sketch0.add(loop0).extrude(-0.06205157300735562)
