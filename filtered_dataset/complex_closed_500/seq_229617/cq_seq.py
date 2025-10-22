import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.11999, -0.0101).lineTo(0.11699, -0.0101).lineTo(0.11699, -0.006).lineTo(0.11999, -0.006).lineTo(0.11999, -0.0101).close()
solid=wp_sketch0.add(loop0).extrude(0.0008668680218097808)
