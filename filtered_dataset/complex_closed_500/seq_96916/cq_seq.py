import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.07116, -0.04514).lineTo(0.04597, -0.04514).threePointArc((0.05304, -0.04221), (0.05597, -0.03514)).lineTo(0.05597, 0.00548).threePointArc((0.05304, 0.01255), (0.04597, 0.01548)).lineTo(0.03035, 0.01548).lineTo(0.03035, 0.01148).lineTo(0.04597, 0.01148).threePointArc((0.05021, 0.00972), (0.05197, 0.00548)).lineTo(0.05197, -0.03514).threePointArc((0.05021, -0.03938), (0.04597, -0.04114)).lineTo(-0.07116, -0.04114).lineTo(-0.07116, -0.04514).close()
solid=wp_sketch0.add(loop0).extrude(-0.222957187242121)
