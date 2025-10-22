import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.079, -0.0715).lineTo(0.077, -0.0715).lineTo(0.077, -0.0465).lineTo(-0.079, -0.0465).lineTo(-0.079, -0.0715).close()
solid=wp_sketch0.add(loop0).extrude(-0.09661125929116154)
