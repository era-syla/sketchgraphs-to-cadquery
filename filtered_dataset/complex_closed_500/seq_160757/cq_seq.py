import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09185, 0.08).lineTo(-0.01185, 0.08).lineTo(-0.01185, 0.077).threePointArc((-0.06629, 0.05445), (-0.08885, 0.0)).lineTo(-0.09185, 0.0).lineTo(-0.09185, 0.08).close()
solid=wp_sketch0.add(loop0).extrude(-0.20387416237103906)
