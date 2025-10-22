import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.14282, 0.01905).lineTo(-0.11742, 0.01905).threePointArc((-0.11293, 0.01719), (-0.11107, 0.0127)).lineTo(-0.11107, -0.0127).threePointArc((-0.11293, -0.01719), (-0.11742, -0.01905)).lineTo(-0.14282, -0.01905).threePointArc((-0.14731, -0.01719), (-0.14917, -0.0127)).lineTo(-0.14917, 0.0127).threePointArc((-0.14731, 0.01719), (-0.14282, 0.01905)).close()
solid=wp_sketch0.add(loop0).extrude(0.040160289840253105)
