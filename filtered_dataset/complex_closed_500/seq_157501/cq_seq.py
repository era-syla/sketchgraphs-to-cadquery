import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.084, 0.05).lineTo(-0.083, 0.05).lineTo(-0.083, -0.052).lineTo(0.084, -0.052).lineTo(0.084, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(-0.44531793880968223)
