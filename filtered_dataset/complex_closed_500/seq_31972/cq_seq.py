import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0275).threePointArc((-0.005, 0.0225), (0.0, 0.0175)).lineTo(0.0, 0.0).lineTo(-0.0175, 0.0).lineTo(-0.0175, 0.018).lineTo(-0.003, 0.0315).lineTo(-0.0, 0.0315).lineTo(0.0, 0.0275).close()
solid=wp_sketch0.add(loop0).extrude(0.0803884091976021)
