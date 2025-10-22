import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02448, 0.01058).lineTo(0.02722, 0.01058).lineTo(0.02722, -0.01058).lineTo(-0.02448, -0.01058).lineTo(-0.02448, 0.01058).close()
solid=wp_sketch0.add(loop0).extrude(0.09047133634101442)
