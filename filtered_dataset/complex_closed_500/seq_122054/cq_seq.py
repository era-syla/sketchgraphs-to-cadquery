import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.50988, 3.1).lineTo(1.56988, 3.1).lineTo(1.56988, 2.36).lineTo(2.84988, 2.36).lineTo(2.84988, 3.1).lineTo(2.90988, 3.1).lineTo(2.90988, 2.3).lineTo(1.50988, 2.3).lineTo(1.50988, 3.1).close()
solid=wp_sketch0.add(loop0).extrude(3.309160606030115)
