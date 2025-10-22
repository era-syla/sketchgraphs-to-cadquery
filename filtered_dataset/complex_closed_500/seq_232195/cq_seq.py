import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.002, 0.01054).lineTo(-0.002, 0.01054).lineTo(-0.002, 0.006).lineTo(0.002, 0.006).lineTo(0.002, 0.01054).close()
solid=wp_sketch0.add(loop0).extrude(0.007700767277646453)
