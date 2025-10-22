import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.12065, 0.00318).threePointArc((-0.13334, -0.01005), (-0.11959, -0.02218)).lineTo(0.06985, -0.00635).lineTo(0.06985, 0.00318).lineTo(-0.12065, 0.00318).close()
solid=wp_sketch0.add(loop0).extrude(0.5457389151962335)
