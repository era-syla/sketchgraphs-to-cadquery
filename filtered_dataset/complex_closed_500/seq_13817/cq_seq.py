import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00318, 0.0).lineTo(0.02774, 0.0).threePointArc((0.02998, 0.00093), (0.03091, 0.00317)).lineTo(0.03091, 0.06783).threePointArc((0.02998, 0.07007), (0.02774, 0.071)).lineTo(0.00318, 0.071).threePointArc((0.00093, 0.07007), (-0.0, 0.06783)).lineTo(0.0, 0.00317).threePointArc((0.00093, 0.00093), (0.00318, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.16338848788270818)
