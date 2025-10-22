import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.15812, 0.01969).lineTo(-0.15812, 0.01969).threePointArc((-0.1778, 0.0), (-0.15812, -0.01969)).lineTo(0.15812, -0.01969).threePointArc((0.1778, 0.0), (0.15812, 0.01969)).close()
solid=wp_sketch0.add(loop0).extrude(0.10471870594419633)
