import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.015, 0.0225).lineTo(0.0025, 0.0225).threePointArc((0.00604, 0.02104), (0.0075, 0.0175)).lineTo(0.0075, -0.0025).threePointArc((0.00604, -0.00604), (0.0025, -0.0075)).lineTo(-0.015, -0.0075).lineTo(-0.015, 0.0225).close()
solid=wp_sketch0.add(loop0).extrude(0.04216957369431722)
