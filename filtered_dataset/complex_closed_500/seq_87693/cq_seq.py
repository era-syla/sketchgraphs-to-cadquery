import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.2286, -0.0508).lineTo(0.2286, -0.0508).lineTo(0.2286, 0.0508).lineTo(-0.2286, 0.0508).lineTo(-0.2286, -0.0508).close()
solid=wp_sketch0.add(loop0).extrude(0.11189818531008804)
