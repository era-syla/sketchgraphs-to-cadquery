import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00476, 0.00314).lineTo(0.00552, 0.00314).lineTo(0.00552, -0.00314).lineTo(0.00476, -0.00314).lineTo(0.00476, 0.0).lineTo(0.00476, 0.00314).close()
solid=wp_sketch0.add(loop0).extrude(-0.0007688057973606806)
