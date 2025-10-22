import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0075, -0.95).lineTo(0.0075, -0.95).lineTo(0.0075, -0.15).lineTo(-0.0075, -0.15).lineTo(-0.0075, -0.95).close()
solid=wp_sketch0.add(loop0).extrude(0.8411338585220434)
