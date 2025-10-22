import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01905, -0.6477).lineTo(0.01905, -0.6477).lineTo(0.01905, 0.6477).lineTo(-0.01905, 0.6477).lineTo(-0.01905, -0.6477).close()
solid=wp_sketch0.add(loop0).extrude(-0.36493136199977755)
