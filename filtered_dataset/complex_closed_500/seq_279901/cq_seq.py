import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05469, 0.07906).lineTo(-0.04958, 0.0829).lineTo(0.01266, -0.0).lineTo(0.01266, -0.029).lineTo(0.00466, -0.029).lineTo(0.00466, 0.0).lineTo(-0.05469, 0.07906).close()
solid=wp_sketch0.add(loop0).extrude(0.26141143330474187)
