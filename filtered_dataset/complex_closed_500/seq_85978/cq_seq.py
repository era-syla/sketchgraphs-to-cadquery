import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00712, 0.0127).lineTo(-0.00712, 0.0381).threePointArc((-0.00526, 0.04259), (-0.00077, 0.04445)).lineTo(0.07543, 0.04445).threePointArc((0.07992, 0.04259), (0.08178, 0.0381)).lineTo(0.08178, 0.0127).threePointArc((0.07992, 0.00821), (0.07543, 0.00635)).lineTo(-0.00077, 0.00635).threePointArc((-0.00526, 0.00821), (-0.00712, 0.0127)).close()
solid=wp_sketch0.add(loop0).extrude(0.19136799035857147)
