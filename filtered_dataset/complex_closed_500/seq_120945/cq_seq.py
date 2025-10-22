import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02584, 0.0).lineTo(0.02496, 0.0).lineTo(0.02386, 0.00625).lineTo(-0.01949, 0.011).lineTo(-0.02584, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.003022399288006288)
