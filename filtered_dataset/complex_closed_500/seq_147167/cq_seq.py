import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00258, -0.01608).lineTo(0.00592, -0.01608).lineTo(0.00592, -0.02258).lineTo(-0.00258, -0.02258).lineTo(-0.00258, -0.01608).close()
solid=wp_sketch0.add(loop0).extrude(-0.011132484294131101)
