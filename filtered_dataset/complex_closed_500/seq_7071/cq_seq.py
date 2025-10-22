import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05448, 0.02217).lineTo(-0.01448, 0.02217).lineTo(-0.01448, -0.01783).lineTo(-0.05448, -0.01783).lineTo(-0.05448, 0.02217).close()
solid=wp_sketch0.add(loop0).extrude(0.055677767161068134)
