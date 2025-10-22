import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.022, -0.005).lineTo(-0.005, -0.005).lineTo(-0.005, -0.0003).lineTo(-0.005, 0.029).lineTo(-0.0003, 0.029).lineTo(0.022, 0.029).lineTo(0.022, 0.0243).lineTo(-0.0003, 0.0243).lineTo(-0.0003, -0.0003).lineTo(0.022, -0.0003).lineTo(0.022, -0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.09659229685575477)
