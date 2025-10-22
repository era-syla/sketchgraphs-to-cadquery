import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.068, 0.027).lineTo(0.066, 0.027).lineTo(0.066, 0.029).lineTo(0.068, 0.029).lineTo(0.068, 0.027).close()
solid=wp_sketch0.add(loop0).extrude(0.0021780713448445862)
