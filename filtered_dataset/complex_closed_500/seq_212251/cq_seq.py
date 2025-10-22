import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09913, 0.00919).lineTo(-0.10873, 0.00919).lineTo(-0.10873, -0.00355).lineTo(-0.09913, -0.00355).lineTo(-0.09913, 0.00919).close()
solid=wp_sketch0.add(loop0).extrude(-0.009727636181736202)
