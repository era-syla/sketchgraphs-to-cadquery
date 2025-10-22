import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00082, 0.00634).lineTo(0.00472, 0.00431).lineTo(0.00358, 0.00211).threePointArc((0.00349, 0.00205), (0.0034, 0.0021)).threePointArc((0.00185, 0.00355), (-0.00023, 0.00399)).threePointArc((-0.00032, 0.00404), (-0.00032, 0.00414)).lineTo(0.00082, 0.00634).close()
solid=wp_sketch0.add(loop0).extrude(-0.001269632296187251)
