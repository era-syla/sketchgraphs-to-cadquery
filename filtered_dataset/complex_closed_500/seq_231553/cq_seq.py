import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.042, 0.034).lineTo(0.0, 0.034).lineTo(0.0, 0.02862).lineTo(-0.042, 0.02862).lineTo(-0.042, 0.034).close()
solid=wp_sketch0.add(loop0).extrude(-0.11143472389793488)
