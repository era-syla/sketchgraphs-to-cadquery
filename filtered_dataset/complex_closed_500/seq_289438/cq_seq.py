import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00199, 0.0039).lineTo(0.01099, 0.0039).lineTo(0.01099, 0.0).lineTo(0.00199, 0.0).lineTo(0.00199, 0.0039).close()
solid=wp_sketch0.add(loop0).extrude(0.0012619709741280361)
