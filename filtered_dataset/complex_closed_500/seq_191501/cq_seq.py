import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02, 0.025).lineTo(-0.0, 0.025).threePointArc((0.00354, 0.02354), (0.005, 0.02)).lineTo(0.005, -0.0).threePointArc((0.00354, -0.00354), (-0.0, -0.005)).lineTo(-0.02, -0.005).lineTo(-0.02, 0.025).close()
solid=wp_sketch0.add(loop0).extrude(0.07620123132968805)
