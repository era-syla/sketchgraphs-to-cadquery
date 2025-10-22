import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00605, 0.0).lineTo(-0.00616, 0.0).lineTo(-0.00616, -0.008).lineTo(0.00605, -0.008).lineTo(0.00605, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.027259092902418913)
