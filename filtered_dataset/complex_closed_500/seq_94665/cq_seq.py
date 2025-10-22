import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01179, 0.03361).lineTo(0.00345, 0.03361).threePointArc((0.00588, 0.0326), (0.00688, 0.03018)).lineTo(0.00688, 0.00878).lineTo(-0.01179, 0.00878).lineTo(-0.01179, 0.03361).close()
solid=wp_sketch0.add(loop0).extrude(0.07361156307511366)
