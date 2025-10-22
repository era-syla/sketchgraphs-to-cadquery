import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.46761, 0.52464).lineTo(0.47885, 0.49682).threePointArc((0.43746, 0.47901), (0.39692, 0.45935)).lineTo(0.38416, 0.49092).lineTo(0.46761, 0.52464).close()
solid=wp_sketch0.add(loop0).extrude(-0.12933700270241963)
