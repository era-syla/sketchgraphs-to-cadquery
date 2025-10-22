import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00953, 0.0).threePointArc((0.00674, 0.00674), (0.0, 0.00953)).lineTo(0.0, 0.0).lineTo(0.00953, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.020633108293633153)
