import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06, -0.0).threePointArc((0.0, 0.06), (-0.06, 0.0)).lineTo(-0.06, -0.05).lineTo(-0.04003, -0.03495).lineTo(-0.01003, -0.03495).lineTo(-0.01003, -0.05495).lineTo(0.01997, -0.05495).lineTo(0.01997, -0.025).lineTo(0.06, -0.025).lineTo(0.06, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.08391158105439313)
