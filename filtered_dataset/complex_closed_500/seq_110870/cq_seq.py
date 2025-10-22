import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.003, 0.04).lineTo(-0.0026, 0.04).lineTo(-0.0026, 0.0).lineTo(-0.003, 0.0).lineTo(-0.003, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.11228681271554948)
