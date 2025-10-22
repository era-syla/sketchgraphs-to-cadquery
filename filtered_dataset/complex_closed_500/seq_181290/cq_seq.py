import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05, 0.0).lineTo(-0.025, 0.0).lineTo(-0.025, -0.005).lineTo(-0.02, -0.005).lineTo(-0.02, 0.0).threePointArc((0.0, 0.02), (0.02, 0.0)).lineTo(0.02, -0.005).lineTo(0.025, -0.005).lineTo(0.025, 0.0).lineTo(0.05, 0.0).lineTo(0.05, 0.01).lineTo(0.02828, 0.01).threePointArc((-0.0, 0.03), (-0.02828, 0.01)).lineTo(-0.05, 0.01).lineTo(-0.05, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.2706926378991907)
