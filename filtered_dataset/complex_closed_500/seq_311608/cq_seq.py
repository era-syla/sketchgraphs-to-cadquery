import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(3.9624, 0.0).lineTo(3.8735, 0.0).lineTo(3.8735, 0.0381).lineTo(3.9624, 0.0381).lineTo(3.9624, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0494313681749591)
