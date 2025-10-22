import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04837, -0.04308).lineTo(0.04837, -0.04308).lineTo(0.00771, 0.03565).lineTo(-0.00772, 0.03565).lineTo(-0.04837, -0.04308).close()
solid=wp_sketch0.add(loop0).extrude(0.0961171056023766)
