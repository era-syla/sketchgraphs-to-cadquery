import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.21857, -0.12788).lineTo(-0.21323, -0.12788).lineTo(-0.21323, 0.18148).lineTo(0.21857, 0.18148).lineTo(0.21857, -0.12788).close()
solid=wp_sketch0.add(loop0).extrude(1.2281113452077919)
