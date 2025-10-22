import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00275, 0.003).lineTo(0.00318, 0.00257).lineTo(0.00318, 0.00043).lineTo(0.00275, -0.0).lineTo(0.00398, 0.0).lineTo(0.00398, 0.003).lineTo(0.00275, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.007457314063154897)
