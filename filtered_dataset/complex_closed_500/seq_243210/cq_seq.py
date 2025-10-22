import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02023, -0.0015).lineTo(0.02034, -0.0015).lineTo(0.02034, 0.0015).lineTo(-0.02023, 0.0015).lineTo(-0.02023, -0.0015).close()
solid=wp_sketch0.add(loop0).extrude(0.033164510700506064)
