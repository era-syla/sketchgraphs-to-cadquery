import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02104, 0.21).lineTo(0.01896, 0.21).lineTo(0.01896, 0.165).threePointArc((0.01457, 0.15439), (0.00396, 0.15)).lineTo(-0.00604, 0.15).threePointArc((-0.01665, 0.15439), (-0.02104, 0.165)).lineTo(-0.02104, 0.21).close()
solid=wp_sketch0.add(loop0).extrude(-0.09685137038557795)
