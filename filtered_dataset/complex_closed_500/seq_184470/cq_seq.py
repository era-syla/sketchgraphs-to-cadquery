import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.008, -0.00185).lineTo(-0.029, -0.00185).lineTo(-0.029, -0.00515).lineTo(-0.008, -0.00515).lineTo(-0.008, -0.00185).close()
solid=wp_sketch0.add(loop0).extrude(0.011771913237142733)
