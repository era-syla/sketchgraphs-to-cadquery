import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0165, 0.023).lineTo(0.0295, 0.023).lineTo(0.0295, 0.016).lineTo(0.0165, 0.016).lineTo(0.0165, 0.023).close()
solid=wp_sketch0.add(loop0).extrude(-0.015700136825842797)
