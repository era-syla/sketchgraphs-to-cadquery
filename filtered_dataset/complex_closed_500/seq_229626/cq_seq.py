import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-3.3528, 1.9812).lineTo(-3.3274, 1.9812).lineTo(-3.3274, 0.0762).lineTo(-3.3528, 0.0762).lineTo(-3.3528, 1.9812).close()
solid=wp_sketch0.add(loop0).extrude(-1.5863333719605195)
