import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1905, -0.12383).lineTo(-0.1397, -0.12383).lineTo(-0.1397, -0.11748).lineTo(-0.1905, -0.11748).lineTo(-0.1905, -0.12383).close()
solid=wp_sketch0.add(loop0).extrude(0.06514834677780033)
