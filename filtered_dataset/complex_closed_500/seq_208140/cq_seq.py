import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00357, 0.00034).lineTo(0.01643, 0.00034).lineTo(0.01643, -0.00866).lineTo(-0.00357, -0.00866).lineTo(-0.00357, 0.00034).close()
solid=wp_sketch0.add(loop0).extrude(0.029921705487699485)
