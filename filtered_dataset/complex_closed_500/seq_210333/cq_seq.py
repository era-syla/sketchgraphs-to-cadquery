import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02084, 0.00683).threePointArc((0.01881, 0.0048), (0.02084, 0.00277)).lineTo(0.04234, 0.00277).threePointArc((0.04437, 0.0048), (0.04234, 0.00683)).lineTo(0.02084, 0.00683).close()
solid=wp_sketch0.add(loop0).extrude(-0.05668449709710376)
