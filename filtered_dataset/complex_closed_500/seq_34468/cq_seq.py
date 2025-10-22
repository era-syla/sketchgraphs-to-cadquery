import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0725, -0.027).lineTo(-0.0685, -0.027).lineTo(-0.0685, 0.0002).lineTo(-0.0725, 0.0002).lineTo(-0.0725, -0.027).close()
solid=wp_sketch0.add(loop0).extrude(-0.029282075846618974)
