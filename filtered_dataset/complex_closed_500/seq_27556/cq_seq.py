import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.027, -0.009).lineTo(0.027, -0.009).threePointArc((0.02912, -0.00988), (0.03, -0.012)).lineTo(0.03, -0.049).lineTo(0.0263, -0.049).lineTo(0.0263, -0.0127).lineTo(-0.0263, -0.0127).lineTo(-0.0263, -0.049).lineTo(-0.03, -0.049).lineTo(-0.03, -0.012).threePointArc((-0.02912, -0.00988), (-0.027, -0.009)).close()
solid=wp_sketch0.add(loop0).extrude(-0.03542441222200199)
