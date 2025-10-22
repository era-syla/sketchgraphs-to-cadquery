import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.73245, 0.0).lineTo(0.76755, 0.0).lineTo(0.76755, 0.4).lineTo(-0.73245, 0.4).lineTo(-0.73245, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-2.7351862313892434)
