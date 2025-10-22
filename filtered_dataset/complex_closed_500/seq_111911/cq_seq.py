import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03503, -0.0029).threePointArc((-0.03551, -0.00231), (-0.03618, -0.00194)).lineTo(-0.07289, -0.00194).threePointArc((-0.07435, -0.00257), (-0.07489, -0.00405)).threePointArc((0.075, -0.0), (-0.07489, 0.00406)).threePointArc((-0.07435, 0.00257), (-0.07289, 0.00195)).lineTo(-0.03643, 0.00195).threePointArc((-0.03562, 0.00226), (-0.03503, 0.0029)).threePointArc((-0.00167, 0.03511), (0.0346, 0.00622)).lineTo(0.0626, 0.00622).lineTo(0.0626, -0.00622).lineTo(0.0346, -0.00622).threePointArc((-0.00167, -0.03511), (-0.03503, -0.0029)).close()
solid=wp_sketch0.add(loop0).extrude(-0.15689643102544204)
