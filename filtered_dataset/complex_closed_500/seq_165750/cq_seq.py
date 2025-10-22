import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1995, -0.0135).lineTo(0.204, -0.0135).lineTo(0.204, -0.0045).lineTo(0.1995, -0.0045).lineTo(0.1995, -0.0135).close()
solid=wp_sketch0.add(loop0).extrude(-0.015042958008675644)
