import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.003, 0.004).lineTo(0.003, 0.004).threePointArc((0.00371, 0.00371), (0.004, 0.003)).lineTo(0.004, -0.003).threePointArc((0.00371, -0.00371), (0.003, -0.004)).lineTo(-0.003, -0.004).threePointArc((-0.00371, -0.00371), (-0.004, -0.003)).lineTo(-0.004, 0.003).threePointArc((-0.00371, 0.00371), (-0.003, 0.004)).close()
solid=wp_sketch0.add(loop0).extrude(-0.005397122582361468)
