import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0053, 0.00926).lineTo(0.00035, 0.00431).threePointArc((-0.0, 0.00417), (-0.00035, 0.00431)).lineTo(-0.0053, 0.00926).threePointArc((-0.00748, 0.01401), (-0.00603, 0.01903)).lineTo(-0.00088, 0.02599).threePointArc((-7e-05, 0.0265), (0.0008, 0.0261)).lineTo(0.00603, 0.01902).threePointArc((0.00748, 0.01401), (0.0053, 0.00926)).close()
solid=wp_sketch0.add(loop0).extrude(-0.039435729858076474)
