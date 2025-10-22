import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.002, 0.0).lineTo(0.008, 0.0).lineTo(0.008, 0.15).lineTo(0.002, 0.15).lineTo(0.002, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.09218999817360633)
