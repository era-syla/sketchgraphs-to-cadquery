import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-4.06997, 0.05).lineTo(-3.06997, 0.05).lineTo(-3.06997, -0.05).lineTo(-4.06997, -0.05).lineTo(-4.06997, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(-2.200633913172404)
