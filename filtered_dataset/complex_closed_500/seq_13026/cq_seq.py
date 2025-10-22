import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03137, 0.01047).lineTo(-0.00337, 0.01947).threePointArc((0.0, 0.02), (0.00337, 0.01947)).lineTo(0.03137, 0.01047).threePointArc((0.039, 0.0), (0.03137, -0.01047)).lineTo(0.00337, -0.01947).threePointArc((0.0, -0.02), (-0.00337, -0.01947)).lineTo(-0.03137, -0.01047).threePointArc((-0.039, 0.0), (-0.03137, 0.01047)).close()
solid=wp_sketch0.add(loop0).extrude(0.1787024826036782)
