import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0254, 0.01194).lineTo(0.0254, 0.01194).lineTo(0.0254, 0.01956).lineTo(-0.0254, 0.01956).lineTo(-0.0254, 0.01194).close()
solid=wp_sketch0.add(loop0).extrude(-0.13932458043041707)
