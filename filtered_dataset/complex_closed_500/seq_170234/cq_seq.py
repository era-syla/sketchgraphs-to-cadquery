import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0662, 0.0312).lineTo(0.0662, 0.0312).threePointArc((0.06761, 0.03061), (0.0682, 0.0292)).lineTo(0.0682, -0.0292).threePointArc((0.06761, -0.03061), (0.0662, -0.0312)).lineTo(-0.0662, -0.0312).threePointArc((-0.06761, -0.03061), (-0.0682, -0.0292)).lineTo(-0.0682, 0.0292).threePointArc((-0.06761, 0.03061), (-0.0662, 0.0312)).close()
solid=wp_sketch0.add(loop0).extrude(0.018753080184259915)
