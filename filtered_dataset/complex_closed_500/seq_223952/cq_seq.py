import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-2.17904, 0.5).lineTo(-2.47904, 0.5).lineTo(-2.47904, 0.8).lineTo(-2.17904, 0.8).lineTo(-2.17904, 0.5).close()
solid=wp_sketch0.add(loop0).extrude(0.48583620197657024)
