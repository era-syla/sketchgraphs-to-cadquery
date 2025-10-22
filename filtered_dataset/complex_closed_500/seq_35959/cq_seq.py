import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.18416, 0.01142).threePointArc((-0.19188, 0.00787), (-0.19408, -0.00033)).lineTo(-0.18081, -0.0747).threePointArc((-0.17742, -0.08058), (-0.17105, -0.08294)).lineTo(0.01319, -0.08436).threePointArc((0.01867, -0.08278), (0.02239, -0.07846)).lineTo(0.04241, -0.03383).threePointArc((0.04306, -0.02765), (0.03995, -0.02228)).lineTo(0.00666, 0.00746).threePointArc((0.0036, 0.00933), (8e-05, 0.01)).lineTo(-0.18416, 0.01142).close()
solid=wp_sketch0.add(loop0).extrude(-0.1692057333331331)
