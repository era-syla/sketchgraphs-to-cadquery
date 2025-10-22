import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01397, 0.02794).lineTo(0.01397, 0.02794).lineTo(0.01397, 0.0254).lineTo(-0.01397, 0.0254).lineTo(-0.01397, 0.02794).close()
solid=wp_sketch0.add(loop0).extrude(0.06681790986910555)
