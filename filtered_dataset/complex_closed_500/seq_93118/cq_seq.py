import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06112, 0.10557).lineTo(0.06112, 0.10557).threePointArc((0.115, 0.08325), (0.13732, 0.02937)).lineTo(0.13732, -0.02937).threePointArc((0.115, -0.08325), (0.06112, -0.10557)).lineTo(-0.06112, -0.10557).threePointArc((-0.115, -0.08325), (-0.13732, -0.02937)).lineTo(-0.13732, 0.02937).threePointArc((-0.115, 0.08325), (-0.06112, 0.10557)).close()
solid=wp_sketch0.add(loop0).extrude(-0.20997959836596586)
