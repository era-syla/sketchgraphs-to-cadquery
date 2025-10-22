import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.2286, -0.01829).lineTo(0.2286, -0.00559).lineTo(0.22936, -0.00559).threePointArc((0.23026, -0.00596), (0.23063, -0.00686)).lineTo(0.23063, -0.01829).lineTo(0.2286, -0.01829).close()
solid=wp_sketch0.add(loop0).extrude(-0.014696878510340964)
