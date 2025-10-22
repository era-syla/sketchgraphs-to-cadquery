import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04221, 0.06).lineTo(-0.05021, 0.06).lineTo(-0.05021, 0.068).lineTo(-0.04221, 0.068).lineTo(-0.04221, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(0.00021710165366492637)
