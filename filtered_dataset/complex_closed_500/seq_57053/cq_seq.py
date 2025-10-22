import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0195, -0.0195).lineTo(-0.0195, -0.0195).lineTo(-0.0195, -0.015).lineTo(0.0195, -0.015).lineTo(0.0195, -0.0195).close()
solid=wp_sketch0.add(loop0).extrude(-0.08011155483840832)
