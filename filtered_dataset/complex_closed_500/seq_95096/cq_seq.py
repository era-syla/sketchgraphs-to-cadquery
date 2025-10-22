import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0385, 0.0625).lineTo(-0.0385, 0.0625).threePointArc((-0.04204, 0.06104), (-0.0435, 0.0575)).lineTo(-0.0435, -0.0575).threePointArc((-0.04204, -0.06104), (-0.0385, -0.0625)).lineTo(0.0385, -0.0625).threePointArc((0.04204, -0.06104), (0.0435, -0.0575)).lineTo(0.0435, 0.0575).threePointArc((0.04204, 0.06104), (0.0385, 0.0625)).close()
solid=wp_sketch0.add(loop0).extrude(-0.18126063244608137)
