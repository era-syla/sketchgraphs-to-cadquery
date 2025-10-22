import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.10062, 0.027).lineTo(0.13448, 0.027).lineTo(0.10062, 0.019).lineTo(0.10062, 0.027).close()
solid=wp_sketch0.add(loop0).extrude(-0.0754088912852536)
