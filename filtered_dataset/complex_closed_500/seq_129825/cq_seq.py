import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.0).lineTo(0.00218, -0.0045).threePointArc((0.00029, -0.00499), (-0.00164, -0.00472)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.01036580248085218)
