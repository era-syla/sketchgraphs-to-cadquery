import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.77132, 1.25728).lineTo(-1.38632, 1.25728).lineTo(-1.38632, 0.88728).lineTo(-0.77132, 0.88728).lineTo(-0.77132, 1.25728).close()
solid=wp_sketch0.add(loop0).extrude(0.36919125780283263)
