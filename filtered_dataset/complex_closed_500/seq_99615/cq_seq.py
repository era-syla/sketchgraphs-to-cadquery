import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0075, 0.035).lineTo(0.0225, 0.035).lineTo(0.0225, -0.035).lineTo(-0.0075, -0.035).lineTo(-0.0075, 0.035).close()
solid=wp_sketch0.add(loop0).extrude(0.04184318514330584)
