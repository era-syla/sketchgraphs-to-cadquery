import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.048, 0.002).lineTo(-0.032, 0.002).lineTo(-0.032, 0.0035).lineTo(-0.048, 0.0035).lineTo(-0.048, 0.002).close()
solid=wp_sketch0.add(loop0).extrude(-0.015165190119251094)
