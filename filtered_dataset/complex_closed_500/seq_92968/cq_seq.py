import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0762).lineTo(-0.0, 0.16105).lineTo(0.04681, 0.12743).lineTo(0.05155, 0.09573).lineTo(0.01756, 0.09573).lineTo(0.01756, 0.07415).threePointArc((0.05977, 0.04727), (0.0762, 0.0)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.23046373981556212)
