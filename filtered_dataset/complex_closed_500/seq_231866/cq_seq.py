import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06, -0.0075).threePointArc((-0.0675, -0.0), (-0.06, 0.0075)).lineTo(-0.16, 0.0075).threePointArc((-0.1525, 0.0), (-0.16, -0.0075)).lineTo(-0.06, -0.0075).close()
solid=wp_sketch0.add(loop0).extrude(0.03271398717580727)
