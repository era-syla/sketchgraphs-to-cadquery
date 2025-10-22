import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03239, -0.0).lineTo(-0.03493, 0.01778).lineTo(-0.03747, 0.01778).lineTo(-0.03493, 0.0).lineTo(-0.03239, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0423502711543636)
