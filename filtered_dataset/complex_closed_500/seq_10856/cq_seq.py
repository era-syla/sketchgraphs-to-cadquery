import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0019, 0.0014).lineTo(-0.0019, 0.0014).threePointArc((-0.00197, 0.00137), (-0.002, 0.0013)).lineTo(-0.002, -0.0013).threePointArc((-0.00197, -0.00137), (-0.0019, -0.0014)).lineTo(0.0019, -0.0014).threePointArc((0.00197, -0.00137), (0.002, -0.0013)).lineTo(0.002, 0.0013).threePointArc((0.00197, 0.00137), (0.0019, 0.0014)).close()
solid=wp_sketch0.add(loop0).extrude(0.005928038151105966)
