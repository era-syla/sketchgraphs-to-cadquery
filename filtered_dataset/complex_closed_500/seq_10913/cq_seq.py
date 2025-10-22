import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.044, 0.02223).lineTo(-0.044, 0.02223).threePointArc((-0.04849, 0.02037), (-0.05035, 0.01588)).lineTo(-0.05035, -0.01588).threePointArc((-0.04849, -0.02037), (-0.044, -0.02223)).lineTo(0.044, -0.02223).threePointArc((0.04849, -0.02037), (0.05035, -0.01588)).lineTo(0.05035, 0.01588).threePointArc((0.04849, 0.02037), (0.044, 0.02223)).close()
solid=wp_sketch0.add(loop0).extrude(0.12761111886145404)
