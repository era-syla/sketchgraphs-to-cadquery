import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02997, 0.00825).lineTo(-0.02997, 0.01675).lineTo(-0.02697, 0.01975).lineTo(-0.02697, 0.00525).lineTo(-0.02997, 0.00825).close()
solid=wp_sketch0.add(loop0).extrude(-0.009131387185682223)
