import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.88072, 2.02053).lineTo(-1.31472, 2.02053).lineTo(-1.31472, 1.57453).lineTo(-1.88072, 1.57453).lineTo(-1.88072, 2.02053).close()
solid=wp_sketch0.add(loop0).extrude(0.17705869842647592)
