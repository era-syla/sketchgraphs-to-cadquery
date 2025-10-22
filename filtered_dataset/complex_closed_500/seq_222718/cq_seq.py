import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.186, 0.0).lineTo(-0.165, 0.0).lineTo(-0.165, 0.004).lineTo(-0.186, 0.004).lineTo(-0.186, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.06149019752449412)
