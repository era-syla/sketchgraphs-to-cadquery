import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.05476, 0.012).lineTo(0.01976, 0.012).threePointArc((0.01622, 0.01054), (0.01476, 0.007)).lineTo(0.01476, -0.007).threePointArc((0.01622, -0.01054), (0.01976, -0.012)).lineTo(0.05476, -0.012).threePointArc((0.0583, -0.01054), (0.05976, -0.007)).lineTo(0.05976, 0.007).threePointArc((0.0583, 0.01054), (0.05476, 0.012)).close()
solid=wp_sketch0.add(loop0).extrude(-0.017054411106547002)
