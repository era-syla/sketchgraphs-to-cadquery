import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01219, 0.0).threePointArc((-0.0, 0.01219), (-0.01219, -0.0)).lineTo(-0.03175, 0.0).lineTo(-0.03175, 0.00476).threePointArc((-0.03129, 0.00589), (-0.03016, 0.00635)).lineTo(-0.01762, 0.00635).threePointArc((-0.01472, 0.00705), (-0.01247, 0.00899)).threePointArc((0.0, 0.01537), (0.01247, 0.00899)).threePointArc((0.01472, 0.00705), (0.01762, 0.00635)).lineTo(0.03016, 0.00635).threePointArc((0.03129, 0.00589), (0.03175, 0.00476)).lineTo(0.03175, 0.0).lineTo(0.01219, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.07759961333732159)
