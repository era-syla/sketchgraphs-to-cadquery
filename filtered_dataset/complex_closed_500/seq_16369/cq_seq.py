import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.1).threePointArc((-0.05, 0.05), (0.0, 0.0)).lineTo(-0.0, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(0.12870089515383887)
