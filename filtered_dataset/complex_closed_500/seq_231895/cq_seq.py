import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.01).lineTo(0.072, -0.01).lineTo(0.072, 0.0).threePointArc((0.03836, 0.0193), (0.0, 0.025)).lineTo(0.0, -0.01).close()
solid=wp_sketch0.add(loop0).extrude(-0.19518866529601933)
