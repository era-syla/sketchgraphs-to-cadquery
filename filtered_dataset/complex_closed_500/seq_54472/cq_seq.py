import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.08928, -0.004).lineTo(0.00422, -0.004).lineTo(0.00422, -0.03456).lineTo(-0.08928, -0.03456).lineTo(-0.08928, -0.004).close()
solid=wp_sketch0.add(loop0).extrude(-0.01782647436827775)
