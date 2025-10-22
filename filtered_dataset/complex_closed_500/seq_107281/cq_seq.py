import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.006, 0.005).threePointArc((-0.00548, 0.00231), (-0.004, 0.0)).lineTo(-0.004, -0.00765).lineTo(-0.006, -0.00765).lineTo(-0.006, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.03682970552760906)
