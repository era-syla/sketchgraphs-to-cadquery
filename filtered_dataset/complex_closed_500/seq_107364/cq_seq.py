import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.84603, -0.03865).lineTo(-1.99322, -0.03865).lineTo(-1.99322, 0.05957).lineTo(-0.84603, 0.05957).lineTo(-0.84603, -0.03865).close()
solid=wp_sketch0.add(loop0).extrude(-0.054648327780278214)
