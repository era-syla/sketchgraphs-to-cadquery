import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.084, 0.004).lineTo(0.084, 0.004).lineTo(0.084, -0.004).lineTo(-0.084, -0.004).lineTo(-0.084, 0.004).close()
solid=wp_sketch0.add(loop0).extrude(0.3673723532622982)
