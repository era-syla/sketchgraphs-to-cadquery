import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00332, -0.005).lineTo(-0.00332, -0.005).threePointArc((-0.006, -0.0), (-0.00332, 0.005)).lineTo(0.00332, 0.005).threePointArc((0.006, 0.0), (0.00332, -0.005)).close()
solid=wp_sketch0.add(loop0).extrude(0.019402722802154514)
