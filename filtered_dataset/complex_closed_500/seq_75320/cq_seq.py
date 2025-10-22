import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0125, 0.035).lineTo(0.0125, 0.035).threePointArc((0.01604, 0.03354), (0.0175, 0.03)).lineTo(0.0175, -0.03).threePointArc((0.01604, -0.03354), (0.0125, -0.035)).lineTo(-0.0125, -0.035).threePointArc((-0.01604, -0.03354), (-0.0175, -0.03)).lineTo(-0.0175, 0.03).threePointArc((-0.01604, 0.03354), (-0.0125, 0.035)).close()
solid=wp_sketch0.add(loop0).extrude(-0.05215144607906147)
