import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01132, 0.00712).lineTo(-0.01687, 0.00367).lineTo(-0.01129, 0.0).lineTo(-0.01132, 0.00712).close()
solid=wp_sketch0.add(loop0).extrude(-0.015160341597797765)
