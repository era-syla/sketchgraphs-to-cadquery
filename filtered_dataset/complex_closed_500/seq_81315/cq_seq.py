import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06, 0.0).lineTo(-0.031, 0.0).threePointArc((0.0, 0.031), (0.031, 0.0)).lineTo(0.06, 0.0).lineTo(0.06, 0.052).threePointArc((0.05473, 0.06473), (0.042, 0.07)).lineTo(-0.042, 0.07).threePointArc((-0.05473, 0.06473), (-0.06, 0.052)).lineTo(-0.06, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.2262745373416461)
