import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0034, 0.0).lineTo(0.025, 0.0).lineTo(0.025, 0.00127).lineTo(0.00384, 0.00127).threePointArc((0.00202, 0.0022), (0.0, 0.00252)).lineTo(0.0, 0.00125).threePointArc((0.00181, 0.00093), (0.0034, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.04239644385110561)
