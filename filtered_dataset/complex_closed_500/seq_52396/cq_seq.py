import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.005).lineTo(0.01904, 0.005).lineTo(0.01692, 0.0).threePointArc((0.00902, -0.00149), (0.001, -0.00199)).lineTo(0.0, -0.00199).lineTo(0.0, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.03326786519722504)
