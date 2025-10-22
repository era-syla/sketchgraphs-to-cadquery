import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.002, 0.0).lineTo(0.022, 0.0).threePointArc((0.02341, 0.00059), (0.024, 0.002)).lineTo(0.024, 0.019).threePointArc((0.02341, 0.02041), (0.022, 0.021)).lineTo(0.002, 0.021).threePointArc((0.00059, 0.02041), (-0.0, 0.019)).lineTo(0.0, 0.002).threePointArc((0.00059, 0.00059), (0.002, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.022361061804359126)
