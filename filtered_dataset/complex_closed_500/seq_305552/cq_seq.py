import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.12763, -0.41042).threePointArc((1.18177, -0.20838), (1.2, 0.0)).lineTo(0.075, 0.0).threePointArc((0.07386, -0.01302), (0.07048, -0.02565)).lineTo(1.12763, -0.41042).close()
solid=wp_sketch0.add(loop0).extrude(2.5637119472726217)
