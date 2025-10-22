import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01194, 0.01905).lineTo(-0.00711, 0.01905).lineTo(-0.00711, 0.01295).lineTo(-0.01194, 0.01295).lineTo(-0.01194, 0.01905).close()
solid=wp_sketch0.add(loop0).extrude(-0.005924516940903965)
