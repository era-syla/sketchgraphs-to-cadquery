import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0245, 0.06).lineTo(-0.0225, 0.06).lineTo(-0.0225, -0.06).lineTo(-0.0245, -0.06).lineTo(-0.0245, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(-0.1753875421260235)
