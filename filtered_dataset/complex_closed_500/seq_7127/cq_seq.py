import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05, -0.01703).lineTo(0.05, -0.01703).lineTo(0.05, -0.07703).lineTo(-0.05, -0.07703).lineTo(-0.05, -0.01703).close()
solid=wp_sketch0.add(loop0).extrude(-0.23456383969926264)
