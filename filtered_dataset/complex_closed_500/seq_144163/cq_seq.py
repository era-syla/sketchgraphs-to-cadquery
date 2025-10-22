import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0381, 0.44958).lineTo(-0.2921, 0.00964).lineTo(-0.0381, 0.00964).lineTo(-0.0381, 0.44958).close()
solid=wp_sketch0.add(loop0).extrude(-1.1765408299243816)
