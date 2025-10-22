import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.027, 0.0025).lineTo(0.058, 0.0025).threePointArc((0.05941, 0.00191), (0.06, 0.0005)).lineTo(0.06, -0.0025).threePointArc((0.05941, -0.00391), (0.058, -0.0045)).lineTo(0.027, -0.0045).threePointArc((0.02559, -0.00391), (0.025, -0.0025)).lineTo(0.025, 0.0005).threePointArc((0.02559, 0.00191), (0.027, 0.0025)).close()
solid=wp_sketch0.add(loop0).extrude(-0.08863365282306518)
