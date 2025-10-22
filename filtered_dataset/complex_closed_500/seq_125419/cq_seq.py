import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0041, 0.004).lineTo(0.0041, 0.002).threePointArc((0.00372, 0.003), (0.0041, 0.004)).close()
solid=wp_sketch0.add(loop0).extrude(0.0025747053889653556)
