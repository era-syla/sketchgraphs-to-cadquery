import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.7, 0.25).lineTo(-0.7, 0.25).lineTo(-0.7, -3.1799).lineTo(0.7, 0.2).lineTo(0.7, 0.25).close()
solid=wp_sketch0.add(loop0).extrude(-1.3049436434469093)
