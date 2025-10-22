import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01358, 0.04904).lineTo(-0.01358, 0.04904).lineTo(-0.01358, 0.14026).lineTo(0.01358, 0.14026).lineTo(0.01358, 0.04904).close()
solid=wp_sketch0.add(loop0).extrude(-0.26593059125867863)
