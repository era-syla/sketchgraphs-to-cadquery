import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06212, 0.06367).lineTo(-0.11292, 0.06367).lineTo(-0.11292, -0.10143).lineTo(-0.06212, -0.10143).lineTo(-0.06212, 0.06367).close()
solid=wp_sketch0.add(loop0).extrude(-0.023953838302444682)
