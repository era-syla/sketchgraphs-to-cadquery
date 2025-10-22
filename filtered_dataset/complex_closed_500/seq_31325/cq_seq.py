import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.005, 0.0085).lineTo(0.0, 0.0085).lineTo(0.0, 0.0).lineTo(0.005, 0.0).lineTo(0.005, 0.0025).lineTo(0.03552, 0.0145).lineTo(0.0355, 0.012).lineTo(0.0405, 0.012).lineTo(0.0405, 0.02046).lineTo(0.0355, 0.0205).lineTo(0.0355, 0.018).lineTo(0.005, 0.006).lineTo(0.005, 0.0085).close()
solid=wp_sketch0.add(loop0).extrude(0.07287169142331967)
