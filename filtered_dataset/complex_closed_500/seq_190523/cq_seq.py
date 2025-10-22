import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.064).lineTo(0.096, 0.064).lineTo(0.096, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.064).close()
solid=wp_sketch0.add(loop0).extrude(0.15871188018810206)
