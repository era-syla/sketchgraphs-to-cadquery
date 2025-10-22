import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.02574).lineTo(-0.004, 0.02574).threePointArc((-0.01249, 0.02222), (-0.016, 0.01374)).lineTo(-0.016, 0.00574).threePointArc((-0.01249, -0.00275), (-0.004, -0.00626)).lineTo(0.0, -0.00626).lineTo(-0.0, 0.02574).close()
solid=wp_sketch0.add(loop0).extrude(-0.051357336224663805)
