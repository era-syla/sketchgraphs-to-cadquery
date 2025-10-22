import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.012, 0.03168).lineTo(0.01846, 0.04159).lineTo(0.0098, 0.04348).lineTo(-0.0113, 0.04348).lineTo(-0.04982, 0.03168).lineTo(0.012, 0.03168).close()
solid=wp_sketch0.add(loop0).extrude(-0.17927612023354855)
