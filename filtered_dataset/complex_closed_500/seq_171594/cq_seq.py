import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00929, 0.00318).lineTo(0.01818, 0.00318).lineTo(0.01818, 0.00635).lineTo(0.02326, 0.00635).lineTo(0.02326, 0.01905).threePointArc((0.01373, 0.00953), (0.00421, 0.01905)).lineTo(0.00421, 0.00635).lineTo(0.00929, 0.00635).lineTo(0.00929, 0.00318).close()
solid=wp_sketch0.add(loop0).extrude(-0.004282786288426691)
