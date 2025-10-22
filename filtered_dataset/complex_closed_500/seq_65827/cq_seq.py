import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.037, 0.055).lineTo(0.037, 0.055).threePointArc((0.04973, 0.04973), (0.055, 0.037)).lineTo(0.055, -0.037).threePointArc((0.04973, -0.04973), (0.037, -0.055)).lineTo(-0.037, -0.055).threePointArc((-0.04973, -0.04973), (-0.055, -0.037)).lineTo(-0.055, 0.037).threePointArc((-0.04973, 0.04973), (-0.037, 0.055)).close()
solid=wp_sketch0.add(loop0).extrude(0.16358130814774963)
