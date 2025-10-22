import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.063, 0.00264).lineTo(-0.042, 0.00264).threePointArc((-0.04059, 0.00205), (-0.04, 0.00064)).lineTo(-0.04, -0.0025).threePointArc((-0.04059, -0.00391), (-0.042, -0.0045)).lineTo(-0.063, -0.0045).threePointArc((-0.06441, -0.00391), (-0.065, -0.0025)).lineTo(-0.065, 0.00064).threePointArc((-0.06441, 0.00205), (-0.063, 0.00264)).close()
solid=wp_sketch0.add(loop0).extrude(-0.03451500804065426)
