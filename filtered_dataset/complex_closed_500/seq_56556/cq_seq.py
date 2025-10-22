import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02593, -0.00603).threePointArc((0.01017, 0.00238), (-0.007, 0.00736)).threePointArc((-0.01464, 0.00935), (-0.0219, 0.01249)).lineTo(-0.0219, -0.0012).threePointArc((0.00236, -0.00021), (0.02593, -0.00603)).close()
solid=wp_sketch0.add(loop0).extrude(-0.08762962710856885)
