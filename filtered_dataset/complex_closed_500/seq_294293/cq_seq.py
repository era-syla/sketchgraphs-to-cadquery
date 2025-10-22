import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1905, -0.1905).lineTo(0.1905, -0.1905).lineTo(0.1905, 0.1905).lineTo(-0.1905, 0.1905).lineTo(-0.1905, -0.1905).close()
solid=wp_sketch0.add(loop0).extrude(0.5157486262909332)
