import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02319, 0.0145).lineTo(-0.00731, 0.0145).lineTo(-0.00731, 0.001).lineTo(-0.02319, 0.001).lineTo(-0.02319, 0.0145).close()
solid=wp_sketch0.add(loop0).extrude(-0.03523684961764759)
