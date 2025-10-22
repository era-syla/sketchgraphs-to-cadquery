import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04401, 0.028).lineTo(0.01999, 0.028).threePointArc((0.02494, 0.02595), (0.02699, 0.021)).lineTo(0.02699, -0.019).threePointArc((0.02494, -0.02395), (0.01999, -0.026)).lineTo(-0.04401, -0.026).threePointArc((-0.04896, -0.02395), (-0.05101, -0.019)).lineTo(-0.05101, 0.021).threePointArc((-0.04896, 0.02595), (-0.04401, 0.028)).close()
solid=wp_sketch0.add(loop0).extrude(0.0062691187526546744)
