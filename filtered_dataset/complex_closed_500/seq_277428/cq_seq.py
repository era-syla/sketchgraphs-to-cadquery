import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.042, 0.005).lineTo(0.034, 0.005).lineTo(0.034, 0.01).lineTo(0.042, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.00908863533762098)
