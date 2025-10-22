import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0072, 0.00275).lineTo(0.00825, 0.0017).lineTo(0.01325, 0.0017).lineTo(0.0143, 0.00275).lineTo(0.0143, 0.0036).threePointArc((0.01424, 0.00374), (0.0141, 0.0038)).lineTo(0.0074, 0.0038).threePointArc((0.00726, 0.00374), (0.0072, 0.0036)).lineTo(0.0072, 0.00275).close()
solid=wp_sketch0.add(loop0).extrude(-0.0005069781772789005)
