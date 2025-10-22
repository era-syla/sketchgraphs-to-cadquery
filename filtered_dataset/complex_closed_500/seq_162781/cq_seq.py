import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.22135, 0.11).lineTo(-0.013, 0.03565).lineTo(-0.013, 0.02).lineTo(-0.02865, 0.02).lineTo(-0.237, 0.09435).lineTo(-0.237, 0.11).lineTo(-0.22135, 0.11).close()
solid=wp_sketch0.add(loop0).extrude(-0.6537328185504695)
