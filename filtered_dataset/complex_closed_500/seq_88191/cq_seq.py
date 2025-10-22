import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01015, 0.00831).threePointArc((-0.00509, 0.00771), (0.0, 0.00751)).lineTo(0.0, 0.00831).lineTo(-0.01015, 0.00831).close()
solid=wp_sketch0.add(loop0).extrude(-0.0013837026866155933)
