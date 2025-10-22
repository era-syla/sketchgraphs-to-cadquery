import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.056, 0.034).lineTo(0.056, 0.034).lineTo(0.056, 0.026).lineTo(0.056, -0.034).lineTo(0.048, -0.034).lineTo(0.048, 0.026).lineTo(-0.048, 0.026).lineTo(-0.048, -0.034).lineTo(-0.056, -0.034).lineTo(-0.056, 0.026).lineTo(-0.056, 0.034).close()
solid=wp_sketch0.add(loop0).extrude(-0.15989552773777987)
