import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00933, 0.00813).lineTo(-0.00845, 0.00813).lineTo(-0.00845, 0.00318).lineTo(-0.00933, 0.00318).lineTo(-0.00933, 0.00813).close()
solid=wp_sketch0.add(loop0).extrude(-0.00179124687055973)
