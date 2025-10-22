import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.08626, -0.0).lineTo(0.08626, 0.0).threePointArc((0.08828, 0.00078), (0.08925, 0.00273)).lineTo(0.0922, 0.03519).threePointArc((0.09143, 0.03748), (0.08921, 0.03846)).lineTo(-0.08921, 0.03846).threePointArc((-0.09143, 0.03748), (-0.0922, 0.03519)).lineTo(-0.08925, 0.00273).threePointArc((-0.08828, 0.00078), (-0.08626, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.30695509613373784)
