import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.011).threePointArc((-0.011, -0.0), (0.0, -0.011)).lineTo(0.019, -0.011).threePointArc((0.02177, -0.01184), (0.02361, -0.01406)).threePointArc((0.04799, -0.04468), (0.08479, -0.05801)).threePointArc((0.09181, -0.05861), (0.09764, -0.06255)).lineTo(0.09894, -0.061).threePointArc((0.09245, -0.05672), (0.0847, -0.056)).threePointArc((0.04907, -0.04299), (0.02545, -0.01329)).threePointArc((0.02288, -0.01017), (0.019, -0.009)).lineTo(0.0, -0.009).threePointArc((-0.009, -0.0), (-0.0, 0.009)).lineTo(0.094, 0.009).lineTo(0.094, 0.011).lineTo(0.0, 0.011).close()
solid=wp_sketch0.add(loop0).extrude(0.23611684802839678)
