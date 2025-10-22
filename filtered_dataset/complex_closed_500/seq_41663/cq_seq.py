import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02294, 0.00315).lineTo(0.05431, -0.01768).threePointArc((0.07099, -0.0155), (0.08123, -0.00215)).lineTo(0.09592, -0.00612).threePointArc((0.0975, -0.01227), (0.09803, -0.01861)).lineTo(0.09803, -0.05861).lineTo(-0.08297, -0.05861).threePointArc((-0.0865, -0.05714), (-0.08797, -0.05361)).lineTo(-0.08797, -0.04361).threePointArc((-0.07771, -0.00067), (-0.04915, 0.033)).lineTo(-0.03849, 0.03013).threePointArc((-0.03629, 0.01342), (-0.02294, 0.00315)).close()
solid=wp_sketch0.add(loop0).extrude(0.020529681359322864)
