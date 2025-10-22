import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03848, 0.01255).lineTo(-0.04152, 0.01255).lineTo(-0.04152, 0.05).lineTo(0.03848, 0.05).lineTo(0.03848, 0.01255).close()
solid=wp_sketch0.add(loop0).extrude(-0.06458705107035292)
