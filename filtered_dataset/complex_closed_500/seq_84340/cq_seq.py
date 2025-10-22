import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.015, 0.0).lineTo(0.015, 0.0).threePointArc((0.01641, 0.00059), (0.017, 0.002)).lineTo(0.017, 0.0635).threePointArc((0.0148, 0.0688), (0.0095, 0.071)).lineTo(-0.0095, 0.071).threePointArc((-0.0148, 0.0688), (-0.017, 0.0635)).lineTo(-0.017, 0.002).threePointArc((-0.01641, 0.00059), (-0.015, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.06589624420525149)
