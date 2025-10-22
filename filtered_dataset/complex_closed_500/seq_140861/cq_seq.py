import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05796, -0.03053).threePointArc((0.06282, 0.01859), (-0.06524, -0.00594)).lineTo(0.01059, -0.00594).lineTo(0.01059, -0.03053).lineTo(-0.05796, -0.03053).close()
solid=wp_sketch0.add(loop0).extrude(0.10908640836605518)
