import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.065, -0.0405).lineTo(0.065, -0.0405).threePointArc((0.06747, -0.03947), (0.0685, -0.037)).lineTo(0.0685, 0.037).threePointArc((0.06747, 0.03947), (0.065, 0.0405)).lineTo(-0.065, 0.0405).threePointArc((-0.06747, 0.03947), (-0.0685, 0.037)).lineTo(-0.0685, -0.037).threePointArc((-0.06747, -0.03947), (-0.065, -0.0405)).close()
solid=wp_sketch0.add(loop0).extrude(-0.32927284038188986)
