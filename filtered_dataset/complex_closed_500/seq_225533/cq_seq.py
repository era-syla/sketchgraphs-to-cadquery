import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-6.73, 2.15).lineTo(-7.86, 2.15).lineTo(-7.86, 0.0).lineTo(-6.73, 0.0).lineTo(-6.73, 2.15).close()
solid=wp_sketch0.add(loop0).extrude(-4.80273260793625)
