import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06, 0.0).lineTo(0.06, 0.0).lineTo(0.06, 0.075).threePointArc((0.05854, 0.07854), (0.055, 0.08)).lineTo(-0.055, 0.08).threePointArc((-0.05854, 0.07854), (-0.06, 0.075)).lineTo(-0.06, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.015285165207972204)
