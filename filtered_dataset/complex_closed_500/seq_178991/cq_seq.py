import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00381, 0.00381).lineTo(-0.0, 0.00254).lineTo(-0.0, 0.00381).lineTo(-0.00381, 0.00381).close()
solid=wp_sketch0.add(loop0).extrude(-0.001207682237005865)
