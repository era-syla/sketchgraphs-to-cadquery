import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.01461).lineTo(0.0, 0.01486).lineTo(-0.00013, 0.01474).lineTo(0.0, 0.01461).close()
solid=wp_sketch0.add(loop0).extrude(-0.0004227084364705739)
