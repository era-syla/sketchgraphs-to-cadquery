import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0449, 0.0554).lineTo(-0.0049, 0.0554).lineTo(-0.0049, 0.0254).lineTo(-0.0449, 0.0254).lineTo(-0.0449, 0.0554).close()
solid=wp_sketch0.add(loop0).extrude(-0.06545499481446124)
