import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.135).lineTo(-0.0008, 0.135).lineTo(-0.0008, 0.155).lineTo(0.0, 0.155).lineTo(0.0, 0.135).close()
solid=wp_sketch0.add(loop0).extrude(-0.007158064818593722)
