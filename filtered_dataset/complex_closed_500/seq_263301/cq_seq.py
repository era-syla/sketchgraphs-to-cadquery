import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0075, 0.285).lineTo(0.0075, 0.285).lineTo(0.0075, 0.015).lineTo(-0.0075, 0.015).lineTo(-0.0075, 0.285).close()
solid=wp_sketch0.add(loop0).extrude(-0.27804488858695725)
