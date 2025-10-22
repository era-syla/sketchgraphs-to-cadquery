import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0508, 0.0508).lineTo(0.0508, 0.0508).lineTo(0.0508, 0.0254).lineTo(-0.0508, 0.0254).lineTo(-0.0508, 0.0508).close()
solid=wp_sketch0.add(loop0).extrude(0.2150106993854422)
