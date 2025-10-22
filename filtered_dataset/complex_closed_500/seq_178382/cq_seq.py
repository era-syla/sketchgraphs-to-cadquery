import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1098, 0.0055).lineTo(0.0957, 0.0055).lineTo(0.0957, 0.0075).lineTo(0.1098, 0.0075).lineTo(0.1098, 0.0055).close()
solid=wp_sketch0.add(loop0).extrude(0.03384611983201195)
