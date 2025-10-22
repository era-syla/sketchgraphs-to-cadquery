import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00762, 0.00508).lineTo(-0.00762, 0.00508).lineTo(-0.00762, 0.02032).lineTo(0.00762, 0.02032).lineTo(0.00762, 0.00508).close()
solid=wp_sketch0.add(loop0).extrude(-0.04078419435482942)
