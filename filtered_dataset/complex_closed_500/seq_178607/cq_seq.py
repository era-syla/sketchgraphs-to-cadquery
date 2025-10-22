import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.2425, 0.005).lineTo(-0.2485, 0.005).lineTo(-0.2485, -0.005).lineTo(-0.2425, -0.005).lineTo(-0.2425, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.002072958307646484)
