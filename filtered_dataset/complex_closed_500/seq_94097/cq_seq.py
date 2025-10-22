import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.13916, 0.31275).lineTo(-0.13061, 0.31275).lineTo(-0.13061, -0.06124).lineTo(0.13916, -0.06124).lineTo(0.13916, 0.31275).close()
solid=wp_sketch0.add(loop0).extrude(-0.4945167384987088)
