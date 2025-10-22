import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1586, 0.28765).lineTo(0.15988, 0.28211).threePointArc((0.1601, 0.2818), (0.16048, 0.28174)).lineTo(0.16602, 0.28302).threePointArc((0.16633, 0.28324), (0.16639, 0.28362)).lineTo(0.16511, 0.28916).threePointArc((0.16489, 0.28947), (0.16451, 0.28953)).lineTo(0.15897, 0.28825).threePointArc((0.15866, 0.28803), (0.1586, 0.28765)).close()
solid=wp_sketch0.add(loop0).extrude(0.004451653241842664)
