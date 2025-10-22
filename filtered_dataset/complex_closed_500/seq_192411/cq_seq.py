import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00635, 0.0).lineTo(0.00635, 0.03175).lineTo(0.01524, 0.03175).lineTo(0.01524, 0.0381).lineTo(0.0, 0.0381).lineTo(0.0, 0.0).lineTo(0.00635, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.09773464101576045)
