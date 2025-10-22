import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.007, 0.0263).lineTo(-0.007, 0.0263).threePointArc((-0.00912, 0.02542), (-0.01, 0.0233)).lineTo(-0.01, 0.0067).threePointArc((-0.00912, 0.00458), (-0.007, 0.0037)).lineTo(0.007, 0.0037).threePointArc((0.00912, 0.00458), (0.01, 0.0067)).lineTo(0.01, 0.0233).threePointArc((0.00912, 0.02542), (0.007, 0.0263)).close()
solid=wp_sketch0.add(loop0).extrude(0.04888088080380219)
