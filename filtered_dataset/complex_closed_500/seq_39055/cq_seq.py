import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.005, 0.0041).lineTo(0.04259, 0.01391).threePointArc((0.04701, 0.00052), (0.04284, -0.01295)).lineTo(0.005, -0.00204).lineTo(0.005, 0.0041).close()
solid=wp_sketch0.add(loop0).extrude(-0.09551576668691446)
