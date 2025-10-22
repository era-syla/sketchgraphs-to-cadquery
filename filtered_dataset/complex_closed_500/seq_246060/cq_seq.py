import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00075, 0.0275).lineTo(0.00075, 0.0275).lineTo(0.00075, -0.0275).lineTo(-0.00075, -0.0275).lineTo(-0.00075, 0.0275).close()
solid=wp_sketch0.add(loop0).extrude(-0.10208537163168617)
