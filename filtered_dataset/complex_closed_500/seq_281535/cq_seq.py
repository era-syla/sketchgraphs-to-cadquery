import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0005, 0.01274).threePointArc((4e-05, -0.01275), (0.00042, 0.01274)).lineTo(0.00042, 0.027).lineTo(0.01905, 0.027).lineTo(0.01905, -0.01427).lineTo(0.0381, -0.01427).lineTo(0.0381, -0.02697).lineTo(-0.0381, -0.02697).lineTo(-0.0381, -0.01427).lineTo(-0.01905, -0.01427).lineTo(-0.01905, 0.027).lineTo(-0.0005, 0.027).lineTo(-0.0005, 0.01274).close()
solid=wp_sketch0.add(loop0).extrude(0.09772302057514494)
