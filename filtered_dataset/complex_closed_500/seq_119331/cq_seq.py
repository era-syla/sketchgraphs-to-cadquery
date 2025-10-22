import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0198).lineTo(0.03, 0.0198).lineTo(0.03, 0.015).lineTo(0.003, 0.015).lineTo(0.003, -0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.029576743469957777)
