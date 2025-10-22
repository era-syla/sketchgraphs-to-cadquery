import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0028, 0.03402).lineTo(0.00915, 0.03402).threePointArc((0.0114, 0.03309), (0.01233, 0.03085)).lineTo(0.01233, 0.0245).threePointArc((0.0114, 0.02225), (0.00915, 0.02132)).lineTo(0.0028, 0.02132).threePointArc((0.00056, 0.02225), (-0.00037, 0.0245)).lineTo(-0.00037, 0.03085).threePointArc((0.00056, 0.03309), (0.0028, 0.03402)).close()
solid=wp_sketch0.add(loop0).extrude(0.01937769427524347)
