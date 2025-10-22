import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1325, -0.018).lineTo(0.0225, -0.018).threePointArc((0.01896, -0.01654), (0.0175, -0.013)).lineTo(0.0175, 0.107).threePointArc((0.01896, 0.11054), (0.0225, 0.112)).lineTo(0.1325, 0.112).threePointArc((0.13604, 0.11054), (0.1375, 0.107)).lineTo(0.1375, -0.013).threePointArc((0.13604, -0.01654), (0.1325, -0.018)).close()
solid=wp_sketch0.add(loop0).extrude(-0.22549498027319476)
