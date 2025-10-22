import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0254, -0.00318).lineTo(0.0254, -0.00318).lineTo(0.0254, 0.14922).lineTo(-0.0254, 0.14922).lineTo(-0.0254, -0.00318).close()
solid=wp_sketch0.add(loop0).extrude(0.2030095147834665)
