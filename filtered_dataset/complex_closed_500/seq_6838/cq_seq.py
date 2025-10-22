import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0375, 0.01392).threePointArc((-0.0, 0.04), (-0.0375, 0.01392)).lineTo(-0.0375, -0.0).lineTo(0.0375, 0.0).lineTo(0.0375, 0.01392).close()
solid=wp_sketch0.add(loop0).extrude(0.13931118926877606)
