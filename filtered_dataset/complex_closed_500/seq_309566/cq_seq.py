import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0).lineTo(0.00654, -0.05652).lineTo(0.0403, -0.01072).lineTo(0.03376, 0.0458).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.1228297144470673)
