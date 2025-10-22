import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06985, 0.0).threePointArc((0.00612, 0.02688), (0.06985, 0.0762)).lineTo(-0.06985, 0.0762).lineTo(-0.06985, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.13742379130008966)
