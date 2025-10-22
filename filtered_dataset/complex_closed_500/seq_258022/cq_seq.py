import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.006).lineTo(0.04, 0.006).lineTo(0.04, 0.009).lineTo(0.08, 0.009).lineTo(0.08, 0.006).lineTo(0.119, 0.006).lineTo(0.119, -0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.30591594574480535)
