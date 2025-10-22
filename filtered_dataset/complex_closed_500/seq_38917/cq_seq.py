import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01374, 0.005).threePointArc((0.01462, 0.0), (-0.01374, -0.005)).lineTo(0.01374, -0.005).threePointArc((0.01462, -0.0), (0.01374, 0.005)).lineTo(-0.01374, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.01963504999278989)
