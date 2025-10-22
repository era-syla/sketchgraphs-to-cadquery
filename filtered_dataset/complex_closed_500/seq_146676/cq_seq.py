import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.17, 0.0).lineTo(0.17, 0.14).lineTo(0.0, 0.14).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.24660468524371554)
