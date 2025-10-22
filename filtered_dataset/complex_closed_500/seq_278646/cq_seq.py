import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.039, -0.0).lineTo(-0.039, 0.002).lineTo(-0.019, 0.002).lineTo(-0.019, -0.002).lineTo(-0.039, -0.002).lineTo(-0.039, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.05867034248015319)
