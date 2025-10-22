import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0404, 0.02223).lineTo(-0.0404, 0.02223).threePointArc((-0.04489, 0.02037), (-0.04675, 0.01587)).lineTo(-0.04675, -0.01587).threePointArc((-0.04489, -0.02037), (-0.0404, -0.02223)).lineTo(0.0404, -0.02223).threePointArc((0.04489, -0.02037), (0.04675, -0.01587)).lineTo(0.04675, 0.01587).threePointArc((0.04489, 0.02037), (0.0404, 0.02223)).close()
solid=wp_sketch0.add(loop0).extrude(0.18875175725521162)
