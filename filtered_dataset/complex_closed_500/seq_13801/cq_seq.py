import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01921, 0.01151).lineTo(0.02062, 0.01151).lineTo(0.02062, -0.01239).lineTo(0.01921, -0.01239).lineTo(0.01921, 0.01151).close()
solid=wp_sketch0.add(loop0).extrude(-0.038733014454389446)
