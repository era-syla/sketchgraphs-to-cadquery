import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.013).lineTo(-0.015, 0.013).lineTo(-0.0255, 0.0025).lineTo(-0.0255, -0.0).lineTo(0.0, -0.0).lineTo(0.0, 0.013).close()
solid=wp_sketch0.add(loop0).extrude(0.044461279173567646)
