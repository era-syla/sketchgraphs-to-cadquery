import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01982, 0.00197).threePointArc((-0.02065, 0.00114), (-0.02096, 0.0)).lineTo(-0.02223, 0.0).lineTo(-0.02223, 0.00197).lineTo(-0.02096, 0.00197).lineTo(-0.01982, 0.00197).close()
solid=wp_sketch0.add(loop0).extrude(0.0012396355364049994)
