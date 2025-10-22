import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.1).lineTo(0.007, 0.1).threePointArc((0.01054, 0.09854), (0.012, 0.095)).lineTo(0.012, 0.02).threePointArc((0.01434, 0.01434), (0.02, 0.012)).lineTo(0.095, 0.012).threePointArc((0.09854, 0.01054), (0.1, 0.007)).lineTo(0.1, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.03577584161799546)
