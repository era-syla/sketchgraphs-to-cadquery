import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09688, 0.8025).lineTo(-0.12688, 0.8025).lineTo(-0.12688, 0.8275).lineTo(-0.09688, 0.8275).lineTo(-0.09688, 0.8025).close()
solid=wp_sketch0.add(loop0).extrude(0.050869379489572514)
