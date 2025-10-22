import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00657, -0.0072).threePointArc((0.00975, -0.0), (0.00657, 0.0072)).lineTo(-0.00657, 0.0072).threePointArc((-0.00975, -0.0), (-0.00657, -0.0072)).lineTo(0.00657, -0.0072).close()
solid=wp_sketch0.add(loop0).extrude(0.02826997600066366)
