import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0825, 0.015).lineTo(0.0825, 0.015).lineTo(0.0825, 0.215).lineTo(-0.0825, 0.215).lineTo(-0.0825, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.5511798955477228)
