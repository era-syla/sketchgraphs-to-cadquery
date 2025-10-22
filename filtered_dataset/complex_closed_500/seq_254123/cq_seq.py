import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07124, 0.0).lineTo(0.06351, 0.0).lineTo(0.06351, -0.035).lineTo(-0.07124, -0.035).lineTo(-0.07124, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.14124496440414838)
