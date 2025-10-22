import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1299, 0.09218).lineTo(0.54727, 0.09218).lineTo(0.54727, -0.12164).lineTo(-0.1299, -0.12164).lineTo(-0.1299, 0.09218).close()
solid=wp_sketch0.add(loop0).extrude(0.5981834381681236)
