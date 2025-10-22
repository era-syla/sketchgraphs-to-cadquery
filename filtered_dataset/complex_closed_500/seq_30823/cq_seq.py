import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0159, -0.0079).lineTo(-0.0159, -0.0079).lineTo(-0.0159, 0.0079).lineTo(0.0159, 0.0079).lineTo(0.0159, -0.0079).close()
solid=wp_sketch0.add(loop0).extrude(0.020714481320635445)
