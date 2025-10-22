import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05052, 0.04747).lineTo(-0.05448, 0.04599).lineTo(-0.07544, 0.10222).lineTo(-0.07148, 0.10369).lineTo(-0.05052, 0.04747).close()
solid=wp_sketch0.add(loop0).extrude(-0.029321260581952873)
