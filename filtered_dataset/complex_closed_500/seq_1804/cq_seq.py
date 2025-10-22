import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0575, 0.0195).lineTo(-0.06, 0.0195).lineTo(-0.06, -0.0195).lineTo(-0.0575, -0.0195).lineTo(-0.0575, 0.0195).close()
solid=wp_sketch0.add(loop0).extrude(-0.003753845874784423)
