import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0254, -0.00432).lineTo(0.0, -0.00432).lineTo(0.0, 0.02108).lineTo(-0.0254, 0.02108).lineTo(-0.0254, -0.00432).close()
solid=wp_sketch0.add(loop0).extrude(-0.07188235739960479)
