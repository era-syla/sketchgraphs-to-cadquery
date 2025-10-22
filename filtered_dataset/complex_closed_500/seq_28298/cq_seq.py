import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01395, 0.04435).lineTo(-0.01395, 0.04435).lineTo(-0.01265, 0.04752).lineTo(0.01265, 0.04752).lineTo(0.01395, 0.04435).close()
solid=wp_sketch0.add(loop0).extrude(0.0010205802911077806)
