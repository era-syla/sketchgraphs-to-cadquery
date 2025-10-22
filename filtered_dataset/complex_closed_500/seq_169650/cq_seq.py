import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05335, 0.01535).lineTo(0.05335, 0.01535).lineTo(0.05335, -0.01535).lineTo(-0.05335, -0.01535).lineTo(-0.05335, 0.01535).close()
solid=wp_sketch0.add(loop0).extrude(-0.25362077224918367)
