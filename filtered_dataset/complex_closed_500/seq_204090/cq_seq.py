import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.54006, 0.26375).lineTo(0.44172, -0.35866).lineTo(0.45753, -0.36116).lineTo(0.55626, 0.26375).lineTo(0.54006, 0.26375).close()
solid=wp_sketch0.add(loop0).extrude(0.3149685828012467)
