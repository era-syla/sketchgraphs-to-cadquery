import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01261, 0.13).lineTo(0.01261, 0.13).threePointArc((0.01676, 0.1278), (0.01726, 0.12314)).lineTo(0.00464, 0.09161).threePointArc((-0.0, 0.08846), (-0.00464, 0.09161)).lineTo(-0.01726, 0.12314).threePointArc((-0.01676, 0.1278), (-0.01261, 0.13)).close()
solid=wp_sketch0.add(loop0).extrude(-0.08940205175110395)
