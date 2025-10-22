import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04937, 0.02223).lineTo(-0.04937, 0.02223).threePointArc((-0.05386, 0.02037), (-0.05572, 0.01587)).lineTo(-0.05572, -0.01587).threePointArc((-0.05386, -0.02037), (-0.04937, -0.02223)).lineTo(0.04937, -0.02223).threePointArc((0.05386, -0.02037), (0.05572, -0.01587)).lineTo(0.05572, 0.01587).threePointArc((0.05386, 0.02037), (0.04937, 0.02223)).close()
solid=wp_sketch0.add(loop0).extrude(0.035816329392525346)
