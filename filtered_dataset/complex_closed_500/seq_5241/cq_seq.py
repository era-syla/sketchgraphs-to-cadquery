import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.25, 0.0).lineTo(0.25, 0.0).lineTo(0.25, -0.8).lineTo(-0.25, -0.8).lineTo(-0.25, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.45469859165179405)
