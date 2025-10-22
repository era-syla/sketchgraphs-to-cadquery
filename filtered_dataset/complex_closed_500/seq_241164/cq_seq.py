import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(1.056, 0.03819).lineTo(1.056, 0.03219).lineTo(1.1, 0.03219).lineTo(1.1, -0.01181).lineTo(1.106, -0.01181).lineTo(1.106, 0.03819).lineTo(1.056, 0.03819).close()
solid=wp_sketch0.add(loop0).extrude(-0.12775451458775525)
