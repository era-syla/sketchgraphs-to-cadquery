import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.033, 0.06081).lineTo(-0.033, 0.054).lineTo(-0.0318, 0.054).lineTo(-0.033, 0.06081).close()
solid=wp_sketch0.add(loop0).extrude(-0.007381508003350563)
