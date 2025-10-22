import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(4.2672, 0.0).lineTo(4.2672, 3.6576).lineTo(-0.0, 3.6576).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(4.9466142173807635)
