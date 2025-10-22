import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0295, -0.01258).lineTo(0.0295, -0.01258).lineTo(0.0295, -0.06246).lineTo(-0.0295, -0.06246).lineTo(-0.0295, -0.01258).close()
solid=wp_sketch0.add(loop0).extrude(0.1386969913873203)
