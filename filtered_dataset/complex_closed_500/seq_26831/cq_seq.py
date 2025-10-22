import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04796, 0.0239).lineTo(-0.03788, 0.0239).lineTo(-0.03788, 0.01543).lineTo(-0.04796, 0.01543).lineTo(-0.04796, 0.0239).close()
solid=wp_sketch0.add(loop0).extrude(-0.021728719041988667)
