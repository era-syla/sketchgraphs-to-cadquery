import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.4448, 0.282).lineTo(0.30188, -0.36614).lineTo(0.31751, -0.36958).lineTo(0.46111, 0.28165).lineTo(0.4448, 0.282).close()
solid=wp_sketch0.add(loop0).extrude(-1.3525476590648569)
