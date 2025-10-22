import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.06, 0.06).lineTo(2.14, 0.06).lineTo(2.14, 0.37).lineTo(0.06, 0.37).lineTo(0.06, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(-5.580497367224303)
