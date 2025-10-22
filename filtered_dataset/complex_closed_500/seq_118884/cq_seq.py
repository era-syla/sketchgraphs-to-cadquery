import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.8128).lineTo(0.7112, 0.8128).lineTo(0.7112, 0.6858).lineTo(0.0, 0.6858).lineTo(0.0, 0.8128).close()
solid=wp_sketch0.add(loop0).extrude(1.0210363563466294)
