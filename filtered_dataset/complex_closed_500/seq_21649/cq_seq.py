import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.038, 0.05).lineTo(-0.038, 0.05).threePointArc((-0.04649, 0.04649), (-0.05, 0.038)).lineTo(-0.05, -0.038).threePointArc((-0.04649, -0.04649), (-0.038, -0.05)).lineTo(0.038, -0.05).threePointArc((0.04649, -0.04649), (0.05, -0.038)).lineTo(0.05, 0.038).threePointArc((0.04649, 0.04649), (0.038, 0.05)).close()
solid=wp_sketch0.add(loop0).extrude(-0.04542059844384405)
