import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0087, -0.013).threePointArc((-0.01251, -0.00381), (-0.0217, 0.0)).lineTo(0.0183, -0.0).threePointArc((0.00911, -0.00381), (0.0053, -0.013)).lineTo(0.0053, -0.021).lineTo(-0.0087, -0.021).lineTo(-0.0087, -0.013).close()
solid=wp_sketch0.add(loop0).extrude(0.09297650914034729)
