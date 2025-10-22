import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03802, 0.07124).lineTo(0.07698, 0.07124).lineTo(0.07698, 0.06924).lineTo(-0.03802, 0.06924).lineTo(-0.03802, 0.07124).close()
solid=wp_sketch0.add(loop0).extrude(0.1632690890126823)
