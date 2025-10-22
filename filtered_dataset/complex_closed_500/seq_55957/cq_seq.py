import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00444, 0.01295).lineTo(-0.00444, 0.02057).threePointArc((-0.00742, 0.02776), (-0.01461, 0.03073)).lineTo(-0.05144, 0.03073).threePointArc((-0.05862, 0.02776), (-0.0616, 0.02057)).lineTo(-0.0616, 0.01295).lineTo(-0.00444, 0.01295).close()
solid=wp_sketch0.add(loop0).extrude(-0.10039710648372815)
