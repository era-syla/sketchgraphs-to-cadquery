import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00178, 0.00254).lineTo(-0.00178, 0.00711).lineTo(-0.00381, 0.00254).lineTo(-0.00178, 0.00254).close()
solid=wp_sketch0.add(loop0).extrude(-0.012779380788609051)
