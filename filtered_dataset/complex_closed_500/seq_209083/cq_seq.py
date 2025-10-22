import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(5.54, 14.26).lineTo(6.44, 14.26).lineTo(6.44, 14.2).lineTo(5.54, 14.2).lineTo(5.54, 14.26).close()
solid=wp_sketch0.add(loop0).extrude(-0.6567414442163239)
