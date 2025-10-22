import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.14488, 0.29036).lineTo(0.14859, 0.29121).threePointArc((0.14896, 0.29115), (0.14919, 0.29084)).lineTo(0.14964, 0.28889).threePointArc((0.14957, 0.28851), (0.14926, 0.28829)).lineTo(0.14556, 0.28743).threePointArc((0.14518, 0.2875), (0.14496, 0.28781)).lineTo(0.14451, 0.28976).threePointArc((0.14457, 0.29013), (0.14488, 0.29036)).close()
solid=wp_sketch0.add(loop0).extrude(-0.0019338090281976038)
