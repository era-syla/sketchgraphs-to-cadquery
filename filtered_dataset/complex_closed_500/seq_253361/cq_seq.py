import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02057, -0.15448).lineTo(-0.1163, -0.15448).lineTo(-0.1163, -0.02421).lineTo(-0.02057, -0.02421).lineTo(-0.02057, -0.15448).close()
solid=wp_sketch0.add(loop0).extrude(-0.06297785830558585)
