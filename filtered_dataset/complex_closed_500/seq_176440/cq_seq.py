import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.42586, 0.06).lineTo(0.41971, 0.06).lineTo(0.41971, -0.04012).lineTo(-0.42586, -0.04012).lineTo(-0.42586, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(-1.7036725288558114)
