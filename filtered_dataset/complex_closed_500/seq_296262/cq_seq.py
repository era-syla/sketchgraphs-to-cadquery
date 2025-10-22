import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01484, 0.0).lineTo(-0.01484, 0.00305).threePointArc((-0.01456, 0.00374), (-0.01389, 0.00405)).lineTo(0.00516, 0.005).threePointArc((0.01082, 0.00381), (0.01516, 0.0)).lineTo(-0.01484, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.03271336701251772)
