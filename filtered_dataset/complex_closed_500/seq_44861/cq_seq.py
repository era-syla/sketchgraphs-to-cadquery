import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03448, 0.01459).lineTo(0.03505, 0.01459).lineTo(0.03505, -0.01315).lineTo(-0.03448, -0.01315).lineTo(-0.03448, 0.01459).close()
solid=wp_sketch0.add(loop0).extrude(-0.1749044212519815)
